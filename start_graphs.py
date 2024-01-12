import networkx as nx

from examples import create_graph_4, create_graph_6
from Node import NodeV, NodeE, NodeQ
from group_5.graph6_breaker import break_graph_6_by_nodes
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
    e12 = list(G.nodes)[4]
    v = cut_edge(G, v1, v2, e12)
    v.h = True
    G.nodes[v]['h'] = True
    return G


def get_P3_left():
    def cut(ver1, ver2, edge):
        v = cut_edge(G, ver1, ver2, edge)
        v.h = True
        G.nodes[v]['h'] = True

    G = create_graph_4()
    nodes = list(G.nodes)

    v1 = nodes[2]
    v2 = nodes[1]
    v3 = nodes[0]
    e12 = nodes[5]
    e23 = nodes[4]

    cut(v1, v2, e12)
    cut(v2, v3, e23)

    return G


def get_P4_left():
    def cut(ver1, ver2, edge):
        v = cut_edge(G, ver1, ver2, edge)
        v.h = True
        G.nodes[v]['h'] = True

    G = create_graph_4()
    nodes = list(G.nodes)

    v1 = nodes[2]
    v2 = nodes[1]
    v3 = nodes[0]
    v4 = nodes[3]
    e14 = nodes[6]
    e23 = nodes[4]

    cut(v1, v4, e14)
    cut(v2, v3, e23)

    return G


def get_P7_left():
    G = create_graph_4()

    nodes = list(G.nodes)
    q = next(filter(lambda node: isinstance(node, NodeQ), nodes))

    q.r = False
    G.nodes[q]["r"] = False

    return G


def mark_target_function(graph_left):
    nodes = list(graph_left.nodes)
    q = next(filter(lambda node: isinstance(node, NodeQ), nodes))

    if q is not None:
        q.r = True
        graph_left.nodes[q]["r"] = True

    return q is not None


def get_P9_left():
    G = create_graph_6()
    return G


def get_P10_left():
    G = create_graph_6()
    v1 = list(G.nodes)[0]
    v2 = list(G.nodes)[1]
    e12 = list(G.nodes)[6]
    v = cut_edge(G, v1, v2, e12)
    v.h = True
    G.nodes[v]['h'] = True
    return G


def get_P11_left():
    return break_graph_6_by_nodes(3, 4, 4, 5)


def get_P12_left():
    return break_graph_6_by_nodes(3, 4, 5, 6)


def get_P21_left():
    G = create_graph_6()

    nodes = list(G.nodes)
    q = next(filter(lambda node: isinstance(node, NodeQ), nodes))

    q.r = False
    G.nodes[q]["r"] = False

    return G


def get_P22_left():
    v1 = NodeV(0, 1, False)  # matches third v from presentation and goes to the right
    v2 = NodeV(1, 1, False)
    v3 = NodeV(1, 0, False)
    v4 = NodeV(0, 0, True)  # this is h5
    v5 = NodeV(0, -1, False)
    v6 = NodeV(-1, -1, False)
    v7 = NodeV(-2, -1, False)
    v8 = NodeV(-2, 0, False)
    v9 = NodeV(-2, 1, False)

    G = nx.Graph()

    add_node(G, v1)
    add_node(G, v2)
    add_node(G, v3)
    add_node(G, v4)
    add_node(G, v5)
    add_node(G, v6)
    add_node(G, v7)
    add_node(G, v8)
    add_node(G, v9)

    add_edge(G, v1, v4, False)
    add_edge(G, v4, v5, True)

    add_hyperedge(G, [v1, v2, v3, v4], True)
    add_hyperedge(G, [v1, v4, v5, v6, v7, v8, v9], False)

    return G
