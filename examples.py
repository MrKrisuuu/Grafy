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


def create_flow_starting_graph():
    outside1 = NodeV(-3, 3, False)
    outside2 = NodeV(3, 3, False, True)
    outside3 = NodeV(3, 0, False)
    outside4 = NodeV(3, -3, False)
    outside5 = NodeV(-3, -3, False)
    outside6 = NodeV(-3, 0, False)

    inside1 = NodeV(-1, 1, False)
    inside2 = NodeV(1, 1, False)
    inside3 = NodeV(1.5, 0, False)
    inside4 = NodeV(1, -1, False)
    inside5 = NodeV(-1, -1, False)
    inside6 = NodeV(-1.5, 0, False)

    G = nx.Graph()

    add_node(G, outside1)
    add_node(G, outside2)
    add_node(G, outside3)
    add_node(G, outside4)
    add_node(G, outside5)
    add_node(G, outside6)

    add_node(G, inside1)
    add_node(G, inside2)
    add_node(G, inside3)
    add_node(G, inside4)
    add_node(G, inside5)
    add_node(G, inside6)

    add_edge(G, outside1, outside2, True)
    add_edge(G, outside2, outside3, True, True)
    add_edge(G, outside3, outside4, True)
    add_edge(G, outside4, outside5, True)
    add_edge(G, outside5, outside6, True)
    add_edge(G, outside6, outside1, True)

    add_edge(G, inside1, inside2, False)
    add_edge(G, inside2, inside3, False)
    add_edge(G, inside3, inside4, False)
    add_edge(G, inside4, inside5, False)
    add_edge(G, inside5, inside6, False)
    add_edge(G, inside6, inside1, False)

    add_edge(G, inside1, outside1, False)
    add_edge(G, inside2, outside2, False)
    add_edge(G, inside3, outside3, False)
    add_edge(G, inside4, outside4, False)
    add_edge(G, inside5, outside5, False)
    add_edge(G, inside6, outside6, False)

    add_hyperedge(G, [outside1, outside2, inside1, inside2], False)
    add_hyperedge(G, [outside2, outside3, inside2, inside3], False)
    add_hyperedge(G, [outside3, outside4, inside3, inside4], False)
    add_hyperedge(G, [outside4, outside5, inside4, inside5], False)
    add_hyperedge(G, [outside5, outside6, inside5, inside6], False)
    add_hyperedge(G, [outside6, outside1, inside6, inside1], False)
    add_hyperedge(G, [inside1, inside2, inside3, inside4, inside5, inside6], False)

    return G
