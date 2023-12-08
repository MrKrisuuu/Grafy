import networkx as nx
from random import random

from Node import NodeV, NodeE, NodeQ
from helpers import add_edge, add_hyperedge, add_node


def create_graph_4():

    v1 = NodeV(1, 1, False)
    v2 = NodeV(1, 0, False)
    v3 = NodeV(0, 0, False)
    v4 = NodeV(0, 1, False)

    G = nx.Graph()

    add_node(G, v1)
    add_node(G, v2)
    add_node(G, v3)
    add_node(G, v4)

    add_edge(G, v1, v2, True)
    add_edge(G, v2, v3, True)
    add_edge(G, v3, v4, True)
    add_edge(G, v4, v1, True)

    add_hyperedge(G, [v1, v2, v3, v4], True)

    return G


def create_graph_6():
    v1 = NodeV(1, 1, False)
    v2 = NodeV(1.5, 0, False)
    v3 = NodeV(1, -1, False)
    v4 = NodeV(-1, -1, False)
    v5 = NodeV(-1.5, 0, False)
    v6 = NodeV(-1, 1, False)

    G = nx.Graph()

    add_node(G, v1)
    add_node(G, v2)
    add_node(G, v3)
    add_node(G, v4)
    add_node(G, v5)
    add_node(G, v6)

    add_edge(G, v1, v2, True)
    add_edge(G, v2, v3, True)
    add_edge(G, v3, v4, True)
    add_edge(G, v4, v5, True)
    add_edge(G, v5, v6, True)
    add_edge(G, v6, v1, True)

    add_hyperedge(G, [v1, v2, v3, v4, v5, v6], True)

    return G