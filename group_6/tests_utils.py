import networkx as nx
from Node import NodeV
from helpers import add_node, add_edge, add_hyperedge, cut_edge


def parse_nodes_data(data):
    objects_map = {}

    for e in data:
        dictionary = e[1]
        objects_map[(dictionary["x"], dictionary["y"])] = dictionary

    return objects_map


def compare_graph_elements(test_map, result_map):
    for key, value in test_map.items():
        element = result_map[key]
        if element is None:
            return False
        for (key1, value1), (key2, value2) in zip(element.items(), value.items()):
            if key1 == key2:
                if value1 != value2:
                    return False

    return True


def create_graph_6_with_subgraph():
    v1 = NodeV(1, 1, False)
    v2 = NodeV(1.5, 0, False)
    v3 = NodeV(1, -1, False)
    v4 = NodeV(-1, -1, False)
    v5 = NodeV(-1.5, 0, False)
    v6 = NodeV(-1, 1, False)
    v7 = NodeV(2, 1, False)
    v8 = NodeV(2, 2, False)
    v9 = NodeV(-2, 2, False)

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

    add_edge(G, v1, v2, True)
    add_edge(G, v2, v3, True)
    add_edge(G, v3, v4, True)
    add_edge(G, v4, v5, True)
    add_edge(G, v5, v6, True)
    add_edge(G, v6, v1, True)
    add_edge(G, v1, v7, False)
    add_edge(G, v8, v1, False)
    add_edge(G, v8, v7, False)
    add_edge(G, v9, v6, False)

    add_hyperedge(G, [v1, v2, v3, v4, v5, v6], True)

    return G


def create_graph_6_with_mixed_labels():
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

    add_edge(G, v1, v2, False)
    add_edge(G, v2, v3, True)
    add_edge(G, v3, v4, True)
    add_edge(G, v4, v5, False)
    add_edge(G, v5, v6, True)
    add_edge(G, v6, v1, False)

    add_hyperedge(G, [v1, v2, v3, v4, v5, v6], True)

    return G


def get_node_inserting_func_for_test(graph, previous_node_id, divider, offset):
    previous_node = list(graph.nodes)[previous_node_id]
    following_node = list(graph.nodes)[(previous_node_id + 1) % divider]
    edge_to_break = list(graph.nodes)[previous_node_id + offset]
    return lambda: cut_edge(graph, previous_node, following_node, edge_to_break)


def get_graph_with_hanging_nodes_for_test(result_graph, divider, offset, edges):
    inserting_funcs = [get_node_inserting_func_for_test(result_graph, e, divider, offset) for e in edges]
    for f in inserting_funcs:
        new_node = f()
        new_node.h = True
        result_graph.nodes[new_node]['h'] = True
    return result_graph