import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph_data, path=None, filename="output/route_result.png"):
    G = nx.Graph()

    # Tambahkan node dan edge ke graf
    for node, neighbors in graph_data.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    # Gunakan layout yang lebih teratur
    pos = nx.spring_layout(G, seed=42, k=0.3)  # k menentukan jarak antar node
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(12, 8))  # Perbesar ukuran gambar
    nx.draw(
        G, pos, with_labels=True, 
        node_color='skyblue', node_size=2500, font_size=10, font_weight='bold',
        edge_color='gray', width=1.5
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Jika ada jalur, tambahkan visualisasi jalur
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange', node_size=3000)

    # Tambahkan judul dan margin
    plt.title("Rute Pengiriman Tercepat (UCS)", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()