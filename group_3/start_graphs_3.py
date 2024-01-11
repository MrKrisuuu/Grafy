from examples import create_graph_4
from helpers import cut_edge, add_edge, add_hyperedge, add_node, cut_edge
import networkx as nx
from Node import NodeV, NodeE, NodeQ


def get_P5_left():
    G = create_graph_4()

    v3 = list(G.nodes)[0]
    v2 = list(G.nodes)[1]
    v1 = list(G.nodes)[2]
    v4 = list(G.nodes)[3]

    e23 = list(G.nodes)[4]
    e12 = list(G.nodes)[5]
    e14 = list(G.nodes)[6]
    e43 = list(G.nodes)[7]

    def f(ve1, ve2, ee12):
        v = cut_edge(G, ve1, ve2, ee12)
        v.h = True
        G.nodes[v]['h'] = True

    # e43.b = False
    # G.nodes[e43]['b'] = False
    f(v3, v2, e23)
    f(v1, v2, e12)
    f(v1, v4, e14)

    return G


def get_P6_left():
    G = create_graph_4()
    v3 = list(G.nodes)[0]
    v2 = list(G.nodes)[1]
    v1 = list(G.nodes)[2]
    v4 = list(G.nodes)[3]

    e23 = list(G.nodes)[4]
    e12 = list(G.nodes)[5]
    e14 = list(G.nodes)[6]
    e43 = list(G.nodes)[7]

    def f(ve1, ve2, ee12):
        v = cut_edge(G, ve1, ve2, ee12)
        v.h = True
        G.nodes[v]['h'] = True

    f(v3, v2, e23)
    f(v1, v2, e12)
    f(v1, v4, e14)
    f(v4, v3, e43)

    return G

def get_P8_left():
    v1 = NodeV(0, 0, False)  
    v2 = NodeV(1, 0, False)
    v3 = NodeV(1, 1, False)
    v4 = NodeV(0, 1, False)
    v5 = NodeV(1, 0.5, True)
    v6 = NodeV(2, 0.5, False)
    v7 = NodeV(2, 1, False)

    G = nx.Graph()

    add_node(G, v1)
    add_node(G, v2)
    add_node(G, v3)
    add_node(G, v4)
    add_node(G, v5)
    add_node(G, v6)
    add_node(G, v7)

    add_edge(G, v3, v5, False)
    add_edge(G, v5, v2, False)

    add_hyperedge(G, [v3, v7, v6, v5], True)
    add_hyperedge(G, [v1, v2, v3, v4], False)

    return G