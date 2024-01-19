import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

from Node import NodeV, NodeE, NodeQ


def get_positions(G):
    positions = {}
    for node in G.nodes:
        positions[node] = (node.x, node.y)
    return positions


def draw_graph(G):
    pos = get_positions(G)
    colors = []
    removes = []
    tmp = deepcopy(G)
    pos = get_positions(tmp)
    for node in tmp.nodes:
        if isinstance(node, NodeQ):
            for edge in tmp.edges:
                if node in edge:
                    removes.append(edge)
    for edge in removes:
        tmp.remove_edge(*edge)
    for node in tmp.nodes:
        if isinstance(node, NodeV):
            colors.append("red")
        if isinstance(node, NodeE):
            colors.append("yellow")
        if isinstance(node, NodeQ):
            colors.append("green")
    nx.draw(tmp, pos=pos, with_labels=True, node_color=colors, node_size=10, font_size=10)
    plt.show()
