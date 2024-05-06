import networkx as nx
import random
import json
import matplotlib.pyplot as plt

def generate_dag(n_nodes, n_edges):
    G = nx.DiGraph()
    G.add_nodes_from(range(n_nodes))
    while len(G.edges) < n_edges:
        a, b = random.sample(range(n_nodes), 2)
        if not nx.has_path(G, b, a):
            G.add_edge(a, b, weight=random.randint(1, 10))  # Assign random weights for A* usage
    return G

def graph_to_json(G):
    graph_data = {
        "nodes": list(G.nodes),
        "edges": [{"source": u, "target": v, "weight": d['weight']} for u, v, d in G.edges(data=True)]
    }
    return json.dumps(graph_data, indent=4)

def save_graph_to_file(G, filename):
    json_output = graph_to_json(G)
    with open(filename, 'w') as file:
        file.write(json_output)
    print(f"Graph saved to {filename}")

def visualize_graph(G):
    # Layout for visualizing the graph, 'pos' determines node positions in a hierarchical layout
    pos = nx.layout.spring_layout(G)
    # Draw nodes and edges
    nx.draw(G, pos, node_color='lightblue', with_labels=True, node_size=500, arrowstyle='-|>', arrowsize=10)
    # Draw edge labels to show weights or other edge properties
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Directed Acyclic Graph (DAG) Visualization')
    plt.show()

# Example usage
n_nodes = 10
n_edges = 15
dag = generate_dag(n_nodes, n_edges)
save_graph_to_file(dag, 'dag_graph.json')
visualize_graph(dag)

