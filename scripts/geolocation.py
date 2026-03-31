#!/usr/bin/env python3
"""
claude-sleuth :: geolocation toolkit
Sun position, shadow analysis, EXIF extraction, weather verification,
and reverse geocoding for image/video geolocation.

All computation is local or uses free, no-auth APIs.

Usage:
    from scripts.geolocation import GeoToolkit
    gt = GeoToolkit()
    exif = gt.extract_exif("photo.jpg")
    sun = gt.sun_position(51.5074, -0.1278, "2025-06-15T14:30:00Z")
    weather = gt.historical_weather(51.5074, -0.1278, "2025-06-15")
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

try:
    import exifread
    HAS_EXIFREAD = True
except ImportError:
    HAS_EXIFREAD = False

try:
    from pysolar.solar import get_altitude, get_azimuth
    HAS_PYSOLAR = True
except ImportError:
    HAS_PYSOLAR = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from geopy.geocoders import Nominatim
    HAS_GEOPY = True
except ImportError:
    HAS_GEOPY = False


def dms_to_decimal(dms_value, ref: str) -> Optional[float]:
    """Convert EXIF DMS (degrees/minutes/seconds) to decimal degrees."""
    try:
        d = float(dms_value.values[0].num) / float(dms_value.values[0].den)
        m = float(dms_value.values[1].num) / float(dms_value.values[1].den)
        s = float(dms_value.values[2].num) / float(dms_value.values[2].den)
        decimal = d + m / 60.0 + s / 3600.0
        if ref in ("S", "W"):
            decimal = -decimal
        return decimal
    except (AttributeError, IndexError, ZeroDivisionError):
        return None


class GeoToolkit:
    """Unified geolocation analysis toolkit."""

    def __init__(self):
        self.geocoder = Nominatim(user_agent="claude-sleuth/1.0") if HAS_GEOPY else None

    def extract_exif(self, image_path: str) -> dict:
        """Extract GPS and metadata from image EXIF data."""
        if not HAS_EXIFREAD:
            return {"error": "exifread not installed"}

        path = Path(image_path)
        if not path.exists():
            return {"error": f"File not found: {image_path}"}

        with open(path, "rb") as f:
            tags = exifread.process_file(f, details=False)

        result = {
            "file": str(path),
            "has_gps": False,
            "gps": {},
            "camera": {},
            "datetime": {},
        }

        # GPS extraction
        lat_tag = tags.get("GPS GPSLatitude")
        lat_ref = str(tags.get("GPS GPSLatitudeRef", "N"))
        lon_tag = tags.get("GPS GPSLongitude")
        lon_ref = str(tags.get("GPS GPSLongitudeRef", "E"))

        if lat_tag and lon_tag:
            lat = dms_to_decimal(lat_tag, lat_ref)
            lon = dms_to_decimal(lon_tag, lon_ref)
            if lat is not None and lon is not None:
                result["has_gps"] = True
                result["gps"] = {
                    "latitude": round(lat, 6),
                    "longitude": round(lon, 6),
                }
                alt_tag = tags.get("GPS GPSAltitude")
                if alt_tag:
                    try:
                        alt = float(alt_tag.values[0].num) / float(alt_tag.values[0].den)
                        result["gps"]["altitude_m"] = round(alt, 1)
                    except (AttributeError, ZeroDivisionError):
                        pass

        # Camera info
        result["camera"] = {
            "make": str(tags.get("Image Make", "")),
            "model": str(tags.get("Image Model", "")),
            "software": str(tags.get("Image Software", "")),
        }

        # Date/time
        dt_original = str(tags.get("EXIF DateTimeOriginal", ""))
        dt_digitised = str(tags.get("EXIF DateTimeDigitized", ""))
        result["datetime"] = {
            "original": dt_original,
            "digitised": dt_digitised,
            "gps_date": str(tags.get("GPS GPSDate", "")),
            "gps_time": str(tags.get("GPS GPSTimeStamp", "")),
        }

        return result

    def sun_position(self, lat: float, lon: float, dt_iso: str) -> dict:
        """Calculate sun altitude and azimuth for a given location and time."""
        if not HAS_PYSOLAR:
            return {"error": "pysolar not installed"}

        dt = datetime.fromisoformat(dt_iso.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)

        altitude = get_altitude(lat, lon, dt)
        azimuth = get_azimuth(lat, lon, dt)

        return {
            "latitude": lat,
            "longitude": lon,
            "datetime_utc": dt.isoformat(),
            "sun_altitude_deg": round(altitude, 2),
            "sun_azimuth_deg": round(azimuth, 2),
            "sun_above_horizon": altitude > 0,
        }

    def shadow_length(self, object_height_m: float, sun_altitude_deg: float) -> Optional[float]:
        """Calculate shadow length from object height and sun altitude."""
        if sun_altitude_deg <= 0:
            return None  # Sun below horizon
        return round(object_height_m / math.tan(math.radians(sun_altitude_deg)), 2)

    def shadow_direction(self, sun_azimuth_deg: float) -> float:
        """Shadow direction is opposite to sun azimuth."""
        return (sun_azimuth_deg + 180) % 360

    def historical_weather(self, lat: float, lon: float, date: str) -> dict:
        """Fetch historical weather from Open-Meteo (free, no auth)."""
        if not HAS_REQUESTS:
            return {"error": "requests not installed"}

        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": date,
            "end_date": date,
            "hourly": "temperature_2m,cloudcover,precipitation,windspeed_10m,weathercode",
            "timezone": "UTC",
        }
        try:
            resp = requests.get(url, params=params, timeout=15)
            if resp.status_code != 200:
                return {"error": f"HTTP {resp.status_code}"}
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    def current_weather(self, lat: float, lon: float) -> dict:
        """Fetch current weather from Open-Meteo."""
        if not HAS_REQUESTS:
            return {"error": "requests not installed"}

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
        }
        try:
            resp = requests.get(url, params=params, timeout=15)
            if resp.status_code != 200:
                return {"error": f"HTTP {resp.status_code}"}
            return resp.json().get("current_weather", {})
        except Exception as e:
            return {"error": str(e)}

    def reverse_geocode(self, lat: float, lon: float) -> dict:
        """Reverse geocode coordinates to address."""
        if not self.geocoder:
            # Fallback to Nominatim API directly
            if not HAS_REQUESTS:
                return {"error": "geopy and requests both unavailable"}
            url = "https://nominatim.openstreetmap.org/reverse"
            params = {"lat": lat, "lon": lon, "format": "json"}
            headers = {"User-Agent": "claude-sleuth/1.0"}
            try:
                resp = requests.get(url, params=params, headers=headers, timeout=10)
                return resp.json()
            except Exception as e:
                return {"error": str(e)}

        try:
            location = self.geocoder.reverse(f"{lat}, {lon}", language="en")
            if location:
                return {
                    "address": location.address,
                    "raw": location.raw.get("address", {}),
                }
            return {"address": None}
        except Exception as e:
            return {"error": str(e)}

    def elevation(self, lat: float, lon: float) -> dict:
        """Get elevation from Open-Elevation API."""
        if not HAS_REQUESTS:
            return {"error": "requests not installed"}
        url = "https://api.open-elevation.com/api/v1/lookup"
        params = {"locations": f"{lat},{lon}"}
        try:
            resp = requests.get(url, params=params, timeout=10)
            if resp.status_code != 200:
                return {"error": f"HTTP {resp.status_code}"}
            results = resp.json().get("results", [])
            if results:
                return {"elevation_m": results[0].get("elevation")}
            return {"elevation_m": None}
        except Exception as e:
            return {"error": str(e)}

    def full_analysis(self, image_path: str) -> dict:
        """Complete geolocation analysis pipeline for an image."""
        result = {"image": image_path, "timestamp_utc": datetime.now(timezone.utc).isoformat()}

        # 1. EXIF
        exif = self.extract_exif(image_path)
        result["exif"] = exif

        if not exif.get("has_gps"):
            result["note"] = "No GPS data in EXIF. Manual geolocation required."
            return result

        lat = exif["gps"]["latitude"]
        lon = exif["gps"]["longitude"]

        # 2. Reverse geocode
        result["geocode"] = self.reverse_geocode(lat, lon)

        # 3. Elevation
        result["elevation"] = self.elevation(lat, lon)

        # 4. Sun position at capture time
        dt_str = exif["datetime"].get("original", "")
        if dt_str:
            try:
                dt = datetime.strptime(dt_str, "%Y:%m:%d %H:%M:%S")
                dt_iso = dt.replace(tzinfo=timezone.utc).isoformat()
                result["sun"] = self.sun_position(lat, lon, dt_iso)
            except ValueError:
                result["sun"] = {"error": f"Could not parse datetime: {dt_str}"}

        # 5. Historical weather at capture date
        if dt_str:
            try:
                date_only = dt_str[:10].replace(":", "-")
                result["weather"] = self.historical_weather(lat, lon, date_only)
            except Exception as e:
                result["weather"] = {"error": str(e)}

        return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Geolocation toolkit")
    sub = parser.add_subparsers(dest="command")

    # EXIF extraction
    exif_p = sub.add_parser("exif", help="Extract EXIF GPS data from image")
    exif_p.add_argument("image", help="Image file path")

    # Sun position
    sun_p = sub.add_parser("sun", help="Calculate sun position")
    sun_p.add_argument("lat", type=float)
    sun_p.add_argument("lon", type=float)
    sun_p.add_argument("datetime", help="ISO datetime (e.g. 2025-06-15T14:30:00Z)")

    # Weather
    wx_p = sub.add_parser("weather", help="Historical weather lookup")
    wx_p.add_argument("lat", type=float)
    wx_p.add_argument("lon", type=float)
    wx_p.add_argument("date", help="Date (YYYY-MM-DD)")

    # Full analysis
    full_p = sub.add_parser("analyse", help="Full image geolocation analysis")
    full_p.add_argument("image", help="Image file path")

    args = parser.parse_args()
    gt = GeoToolkit()

    if args.command == "exif":
        print(json.dumps(gt.extract_exif(args.image), indent=2))
    elif args.command == "sun":
        print(json.dumps(gt.sun_position(args.lat, args.lon, args.datetime), indent=2))
    elif args.command == "weather":
        print(json.dumps(gt.historical_weather(args.lat, args.lon, args.date), indent=2))
    elif args.command == "analyse":
        print(json.dumps(gt.full_analysis(args.image), indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
