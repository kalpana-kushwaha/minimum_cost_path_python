import matplotlib.pyplot as plt
import networkx as nx
from kruskal_algo import kruskal_algo


def graph_plt(lst):
    G = nx.Graph()
    G.add_weighted_edges_from(lst)
    elist = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G, seed=7, scale=3)  # positions for all nodes  - seed for reproducibility
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elist, width=6)
    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("on")
    plt.tight_layout()
    plt.show()


def kruskalgraph_plt(l1, l2):  # l1=original edge list ,l2=edge list minimum cost path
    G = nx.Graph()
    G.add_weighted_edges_from(l1)
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    esmall = [(u, v) for (u, v, d) in l2]
    pos = nx.spring_layout(G, seed=7, scale=3)  # positions for all nodes - seed for reproducibility
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="r", style="solid")
    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("on")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    vtx = [0, 1, 2, 3, 4]
    # list-format = [src,dest,weight]
    # original edge list
    edgel = [[0, 1, 1], [0, 4, 7], [1, 4, 5], [1, 2, 4], [1, 3, 3], [2, 3, 2], [3, 4, 6]]
    edgel2 = kruskal_algo(len(vtx), edgel)  # edge list for minimum cost path
    print(edgel2)
    graph_plt(edgel)
    kruskalgraph_plt(edgel, edgel2)
