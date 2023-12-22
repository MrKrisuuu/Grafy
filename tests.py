import random

from Node import NodeV, NodeE, NodeQ
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


def change_r_reverse_test(get_left, P):
    G = get_left()
    for hyperedge in G.nodes:
        if isinstance(hyperedge, NodeQ):
            hyperedge.r = True
            G.nodes[hyperedge]["r"] = True
    if not P.apply(G):
        print(f"change_r_test OK")
        return 1
    else:
        print(f"change_r_test FAILED")
        return 0


DEFAULT_TESTS = (main_test, remove_vertex_test, remove_edge_test, check_coordinates_test, change_r_test)
DEFAULT_MARK_TESTS = (main_test, remove_vertex_test, remove_edge_test, check_coordinates_test, change_r_reverse_test)


def do_tests(get_left, P, tests=DEFAULT_TESTS):
    OK = 0
    for test in tests:
        OK += test(get_left, P)
    print(f"{OK}/{len(tests)}")
