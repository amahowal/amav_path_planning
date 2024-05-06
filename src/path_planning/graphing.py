# Terrible name but this is where I'm going to put graph generating methods
import networkx as nx
import random
import json
import argparse

def generate_graph(n_nodes, n_edges, graph_type, weight_generator=None):
    if graph_type == 'DAG':
        G = nx.DiGraph()
        G.add_nodes_from(range(n_nodes))
        while len(G.edges) < n_edges:
            a, b = random.sample(range(n_nodes), 2)
            if not nx.has_path(G, b, a):
                G.add_edge(a, b, weight=weight_generator() if weight_generator else None)
    elif graph_type == 'undirected':
        G = nx.Graph()
        G.add_nodes_from(range(n_nodes))
        while len(G.edges) < n_edges:
            a, b = random.sample(range(n_nodes), 2)
            if a != b:
                G.add_edge(a, b, weight=weight_generator() if weight_generator else None)
    elif graph_type == 'directed_cyclic':
        G = nx.DiGraph()
        G.add_nodes_from(range(n_nodes))
        while len(G.edges) < n_edges:
            a, b = random.sample(range(n_nodes), 2)
            G.add_edge(a, b, weight=weight_generator() if weight_generator else None)
    else:
        raise ValueError("Unsupported graph type provided.")

    return G

def uniform_weight():
    return random.randint(1, 10)

def heavy_weight():
    return random.randint(50, 100)

def light_weight():
    return random.randint(1, 5)

def graph_to_json(G):
    graph_data = {
        "nodes": list(G.nodes),
        "edges": [{"source": u, "target": v, "weight": d['weight']} for u, v, d in G.edges(data=True) if d.get('weight')]
    }
    return json.dumps(graph_data, indent=4)

def save_graph_to_file(G, filename):
    json_output = graph_to_json(G)
    with open(filename, 'w') as file:
        file.write(json_output)
    print(f"Graph saved to {filename}")