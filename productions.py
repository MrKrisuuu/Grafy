import networkx as nx

from Node import NodeV, NodeE, NodeQ
from helpers import find_main_nodes, find_hanging_nodes, find_edges, find_nodes, cut_edge, find_hyperedge, add_node, add_edge, add_hyperedge
from start_graphs import *


def P(G):
    main_nodes = find_main_nodes(G)
    hanging_nodes = find_hanging_nodes(G, main_nodes)
    for node in hanging_nodes:
        G.nodes[node]["h"] = False
        node.h = False
    edges = find_edges(G)
    new_nodes = []
    new_qs = {}
    for edge in edges:
        (v1, v2) = find_nodes(G, edge)
        if v1 in hanging_nodes or v2 in hanging_nodes:
            if v1 in hanging_nodes:
                if v2 in new_qs:
                    new_qs[v2].append(v1)
                else:
                    new_qs[v2] = [v1]
            if v2 in hanging_nodes:
                if v1 in new_qs:
                    new_qs[v1].append(v2)
                else:
                    new_qs[v1] = [v2]
        else:
            new_v = cut_edge(G, v1, v2, edge)
            new_nodes.append(new_v)
            if v1 in new_qs:
                new_qs[v1].append(new_v)
            else:
                new_qs[v1] = [new_v]
            if v2 in new_qs:
                new_qs[v2].append(new_v)
            else:
                new_qs[v2] = [new_v]

    q = find_hyperedge(G)
    G.remove_node(q)

    middle_v = NodeV(q.x, q.y, False)
    add_node(G, middle_v)
    for node in new_nodes:
        add_edge(G, middle_v, node, False)
    for node in hanging_nodes:
        add_edge(G, middle_v, node, False)

    for node in main_nodes:
        add_hyperedge(G, [middle_v, node] + new_qs[node], False)


def node_match(n1, n2):
    if len(n1) == 0:
        raise Exception("Set the dict!")

    if len(n2) == 0:
        raise Exception("Set the dict!")

    if n1["type"] != n2["type"]:
        return False

    if n1["type"] == "V":
        return n1["h"] == n2["h"]

    if n1["type"] == "E":
        return True

    if n1["type"] == "Q":
        return n1["r"] == n2["r"]


def P1(G):
    # G.remove_node(list(G.nodes)[0])
    # list(G.nodes)[0].h = True
    # G.nodes[(list(G.nodes)[0])]["h"] = True
    if nx.is_isomorphic(G, get_P1(), node_match=node_match):
        P(G)
    else:
        raise Exception("Wrong graph!")


def P2(G):
    if nx.is_isomorphic(G, get_P2(), node_match=node_match):
        P(G)
    else:
        raise Exception("Wrong graph!")

