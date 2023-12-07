import networkx as nx

from examples import create_graph_4, create_graph_6
from Node import NodeV, NodeE, NodeQ
from helpers import add_edge, add_hyperedge, add_node, cut_edge

def test_start():
    v0 = NodeV(0, 1, False)
    v1 = NodeV(1, 1, False)
    v2 = NodeV(2, 1, False)
    v3 = NodeV(2, 0, False)
    v4 = NodeV(1, 0, False)
    v5 = NodeV(0, 0, False)

    G = nx.Graph()

    add_node(G, v0)
    add_node(G, v1)
    add_node(G, v2)
    add_node(G, v3)
    add_node(G, v4)
    add_node(G, v5)

    add_edge(G, v0, v1, True)
    add_edge(G, v1, v2, True)
    add_edge(G, v2, v3, True)
    add_edge(G, v3, v4, True)
    add_edge(G, v4, v5, True)
    add_edge(G, v5, v0, True)
    add_edge(G, v1, v4, False)

    add_hyperedge(G, [v0, v1, v4, v5], True)
    add_hyperedge(G, [v1, v2, v3, v4], True)

    return G


def get_P1_left():
    G = create_graph_4()
    return G


def get_P2_left():
    G = create_graph_4()
    v1 = list(G.nodes)[0]
    v2 = list(G.nodes)[1]
    e = list(G.nodes)[4]
    v = cut_edge(G, v1, v2, e)
    v.h = True
    G.nodes[v]['h'] = True
    return G