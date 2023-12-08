import random

from Node import NodeV, NodeE, NodeQ


def main_test(get_left, P):
    G = get_left()
    if P.apply(G):
        print(f"main_test OK")
        return 1
    else:
        print(f"main_test FAILED")
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


def do_tests(get_left, P):
    OK = 0
    OK += main_test(get_left, P)
    OK += remove_vertex_test(get_left, P)
    OK += remove_edge_test(get_left, P)
    OK += check_coordinates_test(get_left, P)
    OK += change_r_test(get_left, P)
    print(f"{OK}/5")