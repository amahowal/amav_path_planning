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

def main():
    parser = argparse.ArgumentParser(description="Generate different types of graphs and save them as JSON.")
    parser.add_argument('--nodes', type=int, required=True, help='Number of nodes in the graph')
    parser.add_argument('--edges', type=int, required=True, help='Number of edges in the graph')
    parser.add_argument('--graph_type', type=str, choices=['DAG', 'undirected', 'directed_cyclic'], required=True, help='Type of graph to generate')
    parser.add_argument('--weighted', default=True, action='store_true', help='Generate a weighted graph')
    parser.add_argument('--weight_strategy', type=str, choices=['uniform', 'heavy', 'light'], default='uniform', help='Strategy for generating weights')
    parser.add_argument('--filename', type=str, default='graph.json', help='Filename to save the graph')

    args = parser.parse_args()

    weight_generator = None
    if args.weighted:
        weight_strategies = {
            'uniform': uniform_weight,
            'heavy': heavy_weight,
            'light': light_weight
        }
        weight_generator = weight_strategies.get(args.weight_strategy, uniform_weight)

    G = generate_graph(args.nodes, args.edges, args.graph_type, weight_generator)
    save_graph_to_file(G, args.filename)

if __name__ == "__main__":
    main()

