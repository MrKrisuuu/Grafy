import networkx as nx
import matplotlib.pyplot as plt

from Node import NodeV, NodeE, NodeQ


def get_positions(G):
    positions = {}
    for node in G.nodes:
        positions[node] = (node.x, node.y)
    return positions


def draw_graph(G):
    pos = get_positions(G)
    colors = []
    for node in G.nodes:
        if isinstance(node, NodeV):
            colors.append("red")
        if isinstance(node, NodeE):
            colors.append("yellow")
        if isinstance(node, NodeQ):
            colors.append("green")
    nx.draw(G, pos=pos, with_labels=True, node_color=colors)
    plt.show()
