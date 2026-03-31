#!/usr/bin/env python3
"""
claude-sleuth :: network graph builder
OSINT-focused entity graph using NetworkX + pyvis.
POLE data model (Person, Object, Location, Event) with investigative edge types.

Usage:
    from scripts.network_graph import InvestigationGraph
    g = InvestigationGraph("Case 001")
    g.add_person("p1", "John Smith", nationality="GB")
    g.add_organisation("o1", "Acme Corp")
    g.add_edge("p1", "o1", "director_of", weight=0.9)
    g.export_html("network.html")
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import networkx as nx
    HAS_NX = True
except ImportError:
    HAS_NX = False

try:
    from pyvis.network import Network
    HAS_PYVIS = True
except ImportError:
    HAS_PYVIS = False


# POLE+ node types
NODE_TYPES = {
    "person": {"color": "#4A90D9", "shape": "dot", "size": 25},
    "organisation": {"color": "#E74C3C", "shape": "diamond", "size": 30},
    "location": {"color": "#2ECC71", "shape": "triangle", "size": 20},
    "event": {"color": "#F39C12", "shape": "square", "size": 20},
    "object": {"color": "#9B59B6", "shape": "star", "size": 18},
    "domain": {"color": "#1ABC9C", "shape": "dot", "size": 18},
    "email": {"color": "#34495E", "shape": "dot", "size": 15},
    "phone": {"color": "#95A5A6", "shape": "dot", "size": 15},
    "account": {"color": "#E67E22", "shape": "dot", "size": 15},
    "document": {"color": "#8E44AD", "shape": "square", "size": 15},
    "vehicle": {"color": "#D35400", "shape": "triangle", "size": 18},
    "address": {"color": "#27AE60", "shape": "triangle", "size": 15},
}

# Investigative edge types
EDGE_TYPES = {
    "owns": {"color": "#333333", "width": 2},
    "employs": {"color": "#4A90D9", "width": 2},
    "director_of": {"color": "#E74C3C", "width": 3},
    "shareholder_of": {"color": "#C0392B", "width": 2},
    "registered_to": {"color": "#2ECC71", "width": 1},
    "linked_to": {"color": "#95A5A6", "width": 1, "dashes": True},
    "communicates_with": {"color": "#F39C12", "width": 2},
    "related_to": {"color": "#9B59B6", "width": 1},
    "located_at": {"color": "#27AE60", "width": 1},
    "attended": {"color": "#E67E22", "width": 1},
    "uses": {"color": "#1ABC9C", "width": 1},
    "alias_of": {"color": "#E74C3C", "width": 2, "dashes": True},
    "financial_link": {"color": "#C0392B", "width": 3},
    "family": {"color": "#8E44AD", "width": 2},
}


class InvestigationGraph:
    """OSINT investigation graph with POLE data model."""

    def __init__(self, case_name: str = "Investigation"):
        if not HAS_NX:
            raise ImportError("networkx is required: pip install networkx")
        self.graph = nx.Graph()
        self.case_name = case_name
        self.graph.graph["case_name"] = case_name
        self.graph.graph["created_utc"] = datetime.now(timezone.utc).isoformat()

    def _add_node(self, node_id: str, label: str, node_type: str, **attrs):
        style = NODE_TYPES.get(node_type, NODE_TYPES["object"])
        self.graph.add_node(
            node_id,
            label=label,
            node_type=node_type,
            color=style["color"],
            shape=style["shape"],
            size=style["size"],
            **attrs,
        )

    def add_person(self, node_id: str, name: str, **attrs):
        self._add_node(node_id, name, "person", **attrs)

    def add_organisation(self, node_id: str, name: str, **attrs):
        self._add_node(node_id, name, "organisation", **attrs)

    def add_location(self, node_id: str, name: str, **attrs):
        self._add_node(node_id, name, "location", **attrs)

    def add_event(self, node_id: str, name: str, **attrs):
        self._add_node(node_id, name, "event", **attrs)

    def add_domain(self, node_id: str, name: str, **attrs):
        self._add_node(node_id, name, "domain", **attrs)

    def add_email(self, node_id: str, address: str, **attrs):
        self._add_node(node_id, address, "email", **attrs)

    def add_phone(self, node_id: str, number: str, **attrs):
        self._add_node(node_id, number, "phone", **attrs)

    def add_account(self, node_id: str, label: str, **attrs):
        self._add_node(node_id, label, "account", **attrs)

    def add_document(self, node_id: str, label: str, **attrs):
        self._add_node(node_id, label, "document", **attrs)

    def add_vehicle(self, node_id: str, label: str, **attrs):
        self._add_node(node_id, label, "vehicle", **attrs)

    def add_address(self, node_id: str, address: str, **attrs):
        self._add_node(node_id, address, "address", **attrs)

    def add_edge(self, source: str, target: str, edge_type: str, weight: float = 1.0, **attrs):
        style = EDGE_TYPES.get(edge_type, {"color": "#CCCCCC", "width": 1})
        self.graph.add_edge(
            source,
            target,
            edge_type=edge_type,
            weight=weight,
            color=style.get("color", "#CCCCCC"),
            width=style.get("width", 1),
            dashes=style.get("dashes", False),
            title=f"{edge_type} (weight: {weight})",
            **attrs,
        )

    def centrality_report(self) -> dict:
        """Calculate centrality metrics for all nodes."""
        if len(self.graph.nodes) == 0:
            return {"error": "Graph is empty"}

        degree = nx.degree_centrality(self.graph)
        betweenness = nx.betweenness_centrality(self.graph)

        try:
            eigenvector = nx.eigenvector_centrality(self.graph, max_iter=1000)
        except nx.PowerIterationFailedConvergence:
            eigenvector = {n: 0 for n in self.graph.nodes}

        nodes = []
        for node_id in self.graph.nodes:
            data = self.graph.nodes[node_id]
            nodes.append({
                "id": node_id,
                "label": data.get("label", ""),
                "type": data.get("node_type", ""),
                "degree_centrality": round(degree.get(node_id, 0), 4),
                "betweenness_centrality": round(betweenness.get(node_id, 0), 4),
                "eigenvector_centrality": round(eigenvector.get(node_id, 0), 4),
            })

        # Sort by betweenness (bridge nodes)
        nodes.sort(key=lambda x: x["betweenness_centrality"], reverse=True)

        return {
            "case_name": self.case_name,
            "total_nodes": len(self.graph.nodes),
            "total_edges": len(self.graph.edges),
            "connected_components": nx.number_connected_components(self.graph),
            "density": round(nx.density(self.graph), 4),
            "nodes": nodes,
        }

    def community_detection(self) -> dict:
        """Detect communities using Louvain method."""
        try:
            from networkx.algorithms.community import louvain_communities
            communities = louvain_communities(self.graph)
            result = []
            for i, community in enumerate(communities):
                members = []
                for node_id in community:
                    data = self.graph.nodes[node_id]
                    members.append({"id": node_id, "label": data.get("label", "")})
                result.append({"community_id": i, "size": len(community), "members": members})
            return {"communities": result, "count": len(result)}
        except Exception as e:
            return {"error": str(e)}

    def export_html(self, filepath: str, height: str = "800px", width: str = "100%") -> str:
        """Export interactive HTML visualisation via pyvis."""
        if not HAS_PYVIS:
            raise ImportError("pyvis is required: pip install pyvis")

        net = Network(height=height, width=width, notebook=False, directed=False)
        net.from_nx(self.graph)
        net.set_options(json.dumps({
            "physics": {
                "forceAtlas2Based": {
                    "gravitationalConstant": -50,
                    "centralGravity": 0.01,
                    "springLength": 200,
                },
                "solver": "forceAtlas2Based",
            },
            "interaction": {"hover": True, "tooltipDelay": 200},
        }))
        net.save_graph(filepath)
        return filepath

    def export_json(self, filepath: str) -> str:
        """Export graph as JSON (nodes + edges)."""
        data = {
            "case_name": self.case_name,
            "exported_utc": datetime.now(timezone.utc).isoformat(),
            "nodes": [],
            "edges": [],
        }
        for node_id, attrs in self.graph.nodes(data=True):
            node_data = {"id": node_id}
            node_data.update(attrs)
            data["nodes"].append(node_data)
        for u, v, attrs in self.graph.edges(data=True):
            edge_data = {"source": u, "target": v}
            edge_data.update(attrs)
            data["edges"].append(edge_data)

        Path(filepath).write_text(json.dumps(data, indent=2))
        return filepath

    def export_gexf(self, filepath: str) -> str:
        """Export as GEXF for Gephi import."""
        nx.write_gexf(self.graph, filepath)
        return filepath

    def import_json(self, filepath: str):
        """Import from previously exported JSON."""
        data = json.loads(Path(filepath).read_text())
        for node in data.get("nodes", []):
            node_id = node.pop("id")
            self.graph.add_node(node_id, **node)
        for edge in data.get("edges", []):
            source = edge.pop("source")
            target = edge.pop("target")
            self.graph.add_edge(source, target, **edge)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Investigation network graph")
    parser.add_argument("--input", "-i", help="Import JSON graph file")
    parser.add_argument("--html", help="Export HTML visualisation")
    parser.add_argument("--json", help="Export JSON")
    parser.add_argument("--gexf", help="Export GEXF for Gephi")
    parser.add_argument("--centrality", action="store_true", help="Print centrality report")
    parser.add_argument("--communities", action="store_true", help="Detect communities")
    args = parser.parse_args()

    g = InvestigationGraph()
    if args.input:
        g.import_json(args.input)
        print(f"Loaded graph: {len(g.graph.nodes)} nodes, {len(g.graph.edges)} edges")

    if args.centrality:
        print(json.dumps(g.centrality_report(), indent=2))
    if args.communities:
        print(json.dumps(g.community_detection(), indent=2))
    if args.html:
        g.export_html(args.html)
        print(f"HTML exported to {args.html}")
    if args.json:
        g.export_json(args.json)
        print(f"JSON exported to {args.json}")
    if args.gexf:
        g.export_gexf(args.gexf)
        print(f"GEXF exported to {args.gexf}")


if __name__ == "__main__":
    main()
