#!/usr/bin/env python3
"""
claude-sleuth :: financial filing analyser
Anomaly detection on SEC EDGAR filings using edgartools.
Includes Benford's Law analysis, YoY variance detection, and Z-Score.

Usage:
    from scripts.financial_analysis import FinancialAnalyser
    fa = FinancialAnalyser()
    report = fa.analyse_company("AAPL")
"""

import json
import math
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


def benfords_law_test(values: list) -> dict:
    """Test a set of numeric values against Benford's Law distribution.
    Returns chi-squared statistic and per-digit comparison."""
    expected = {d: math.log10(1 + 1 / d) for d in range(1, 10)}

    first_digits = []
    for v in values:
        s = str(abs(v)).lstrip("0").lstrip(".")
        if s and s[0].isdigit() and s[0] != "0":
            first_digits.append(int(s[0]))

    if len(first_digits) < 50:
        return {"error": "Insufficient data points (need 50+)", "count": len(first_digits)}

    n = len(first_digits)
    observed = Counter(first_digits)

    chi_sq = 0
    digits = {}
    for d in range(1, 10):
        obs_freq = observed.get(d, 0) / n
        exp_freq = expected[d]
        chi_sq += ((obs_freq - exp_freq) ** 2) / exp_freq
        digits[str(d)] = {
            "observed": round(obs_freq, 4),
            "expected": round(exp_freq, 4),
            "deviation": round(obs_freq - exp_freq, 4),
        }

    # Chi-squared critical value at p=0.05, df=8 is 15.507
    return {
        "chi_squared": round(chi_sq * n, 4),
        "critical_value_p05": 15.507,
        "passes": (chi_sq * n) < 15.507,
        "sample_size": n,
        "digits": digits,
    }


def yoy_variance(values: list, labels: list, threshold: float = 0.20) -> list:
    """Flag year-over-year changes exceeding threshold."""
    flags = []
    for i in range(1, len(values)):
        if values[i - 1] == 0:
            continue
        change = (values[i] - values[i - 1]) / abs(values[i - 1])
        if abs(change) >= threshold:
            flags.append({
                "period": f"{labels[i-1]} -> {labels[i]}",
                "previous": values[i - 1],
                "current": values[i],
                "change_pct": round(change * 100, 2),
                "flag": "SIGNIFICANT" if abs(change) >= threshold else "normal",
            })
    return flags


def altman_z_score(
    working_capital: float,
    retained_earnings: float,
    ebit: float,
    market_cap: float,
    total_liabilities: float,
    total_assets: float,
    revenue: float,
) -> dict:
    """Altman Z-Score for bankruptcy prediction.
    Z > 2.99: Safe zone
    1.81 < Z < 2.99: Grey zone
    Z < 1.81: Distress zone
    """
    if total_assets == 0:
        return {"error": "Total assets cannot be zero"}

    x1 = working_capital / total_assets
    x2 = retained_earnings / total_assets
    x3 = ebit / total_assets
    x4 = market_cap / total_liabilities if total_liabilities != 0 else 0
    x5 = revenue / total_assets

    z = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5

    if z > 2.99:
        zone = "safe"
    elif z > 1.81:
        zone = "grey"
    else:
        zone = "distress"

    return {
        "z_score": round(z, 4),
        "zone": zone,
        "components": {
            "x1_working_capital_ratio": round(x1, 4),
            "x2_retained_earnings_ratio": round(x2, 4),
            "x3_ebit_ratio": round(x3, 4),
            "x4_market_equity_ratio": round(x4, 4),
            "x5_asset_turnover": round(x5, 4),
        },
    }


class FinancialAnalyser:
    """SEC EDGAR financial analysis with anomaly detection."""

    def __init__(self):
        self.headers = {
            "User-Agent": "claude-sleuth/1.0 (investigation@example.com)",
            "Accept": "application/json",
        }

    def get_company_facts(self, cik: str) -> dict:
        """Fetch XBRL company facts from SEC EDGAR."""
        if not HAS_REQUESTS:
            return {"error": "requests not installed"}
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik.zfill(10)}.json"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}"}
        return resp.json()

    def get_cik_from_ticker(self, ticker: str) -> Optional[str]:
        """Resolve ticker symbol to CIK."""
        if not HAS_REQUESTS:
            return None
        url = "https://www.sec.gov/files/company_tickers.json"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code != 200:
            return None
        tickers = resp.json()
        ticker_upper = ticker.upper()
        for _, entry in tickers.items():
            if entry.get("ticker", "").upper() == ticker_upper:
                return str(entry["cik_str"])
        return None

    def extract_metric_series(self, facts: dict, taxonomy: str, metric: str, unit: str = "USD") -> tuple:
        """Extract a time series of a specific metric from company facts."""
        try:
            entries = facts["facts"][taxonomy][metric]["units"][unit]
        except (KeyError, TypeError):
            return [], []

        # Filter to annual (10-K) filings
        annual = [e for e in entries if e.get("form") == "10-K" and "frame" in e]
        annual.sort(key=lambda x: x.get("end", ""))

        # Deduplicate by frame
        seen = set()
        unique = []
        for e in annual:
            frame = e["frame"]
            if frame not in seen:
                seen.add(frame)
                unique.append(e)

        values = [e["val"] for e in unique]
        labels = [e.get("frame", e.get("end", "")) for e in unique]
        return values, labels

    def analyse_company(self, ticker_or_cik: str) -> dict:
        """Run full financial analysis on a company."""
        # Resolve ticker to CIK if needed
        if ticker_or_cik.isdigit():
            cik = ticker_or_cik
        else:
            cik = self.get_cik_from_ticker(ticker_or_cik)
            if not cik:
                return {"error": f"Could not resolve ticker: {ticker_or_cik}"}

        facts = self.get_company_facts(cik)
        if "error" in facts:
            return facts

        report = {
            "entity": facts.get("entityName", ""),
            "cik": cik,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "analyses": {},
        }

        # Revenue analysis
        revenue_vals, revenue_labels = self.extract_metric_series(
            facts, "us-gaap", "Revenues"
        )
        if not revenue_vals:
            revenue_vals, revenue_labels = self.extract_metric_series(
                facts, "us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax"
            )

        if revenue_vals:
            report["analyses"]["revenue"] = {
                "values": list(zip(revenue_labels, revenue_vals)),
                "yoy_flags": yoy_variance(revenue_vals, revenue_labels),
                "benfords": benfords_law_test(revenue_vals),
            }

        # Net income
        ni_vals, ni_labels = self.extract_metric_series(
            facts, "us-gaap", "NetIncomeLoss"
        )
        if ni_vals:
            report["analyses"]["net_income"] = {
                "values": list(zip(ni_labels, ni_vals)),
                "yoy_flags": yoy_variance(ni_vals, ni_labels),
            }

        # Total assets
        assets_vals, assets_labels = self.extract_metric_series(
            facts, "us-gaap", "Assets"
        )
        if assets_vals:
            report["analyses"]["total_assets"] = {
                "values": list(zip(assets_labels, assets_vals)),
                "yoy_flags": yoy_variance(assets_vals, assets_labels),
            }

        # Collect all financial values for Benford's Law
        all_values = revenue_vals + ni_vals + assets_vals
        if len(all_values) >= 50:
            report["analyses"]["benfords_all_metrics"] = benfords_law_test(all_values)

        return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Financial filing analyser")
    parser.add_argument("ticker", help="Stock ticker or CIK number")
    parser.add_argument("--output", "-o", help="Output JSON file")
    args = parser.parse_args()

    fa = FinancialAnalyser()
    report = fa.analyse_company(args.ticker)

    if args.output:
        Path(args.output).write_text(json.dumps(report, indent=2))
        print(f"Report written to {args.output}")
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
