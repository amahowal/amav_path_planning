import json
import networkx as nx
import matplotlib.pyplot as plt
import argparse

def load_graph_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    
    G = nx.DiGraph()
    for node in data['nodes']:
        G.add_node(node)
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], weight=edge['weight'])
    
    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)  # Positions for all nodes
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500)
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Visualization of the Graph')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Visualize a graph from a JSON file.")
    parser.add_argument('filename', type=str, help='Filename of the graph in JSON format')

    args = parser.parse_args()
    G = load_graph_from_json(args.filename)
    visualize_graph(G)

if __name__ == "__main__":
    main()

