import random

from Node import NodeV, NodeE, NodeQ
from helpers import add_node, add_edge
from utils import draw_graph


def main_test(get_left, P):
    G = get_left()
    draw_graph(G)
    if P.apply(G):
        print(f"main_test OK")
        draw_graph(G)
        return 1
    else:
        print(f"main_test FAILED")
        draw_graph(G)
        return 0


def remove_vertex_test(get_left, P):
    G = get_left()
    nodes = []
    for node in G.nodes:
        if isinstance(node, NodeV):
            nodes.append(node)
    random_node = random.choice(nodes)
    G.remove_node(random_node)
    if not P.apply(G):
        print(f"remove_vertex_test OK")
        return 1
    else:
        print(f"remove_vertex_test FAILED")
        return 0


def remove_edge_test(get_left, P):
    G = get_left()
    edges = []
    for edge in G.nodes:
        if isinstance(edge, NodeE):
            edges.append(edge)
    random_edge = random.choice(edges)
    G.remove_node(random_edge)
    if not P.apply(G):
        print(f"remove_edge_test OK")
        return 1
    else:
        print(f"remove_edge_test FAILED")
        return 0


def check_coordinates_test(get_left, P):
    G = get_left()
    # TODO
    if not P.apply(G):
        print(f"check_coordinates_test OK")
        return 1
    else:
        print(f"check_coordinates_test FAILED")
        return 0


def change_r_test(get_left, P):
    G = get_left()
    for hyperedge in G.nodes:
        if isinstance(hyperedge, NodeQ):
            hyperedge.r = False
            G.nodes[hyperedge]["r"] = False
    if not P.apply(G):
        print(f"change_r_test OK")
        return 1
    else:
        print(f"change_r_test FAILED")
        return 0

def add_node_test(get_left, P):
    G = get_left()

    new_v = NodeV(2, 2, False)

    add_node(G, new_v)

    v0 = list(G.nodes)[0]
    v1 = list(G.nodes)[1]

    add_edge(G, v0, new_v, True)
    add_edge(G, v1, new_v, True)

    draw_graph(G)

    if P.apply(G):
        print(f"add_node_test OK")
        draw_graph(G)
        return 1
    else:
        draw_graph(G)
        print(f"add_node_test FAILED")
        return 0

def do_tests(get_left, P):
    OK = 0
    OK += main_test(get_left, P)
    OK += remove_vertex_test(get_left, P)
    OK += remove_edge_test(get_left, P)
    OK += check_coordinates_test(get_left, P)
    OK += change_r_test(get_left, P)
    OK += add_node_test(get_left, P)
    print(f"{OK}/6")