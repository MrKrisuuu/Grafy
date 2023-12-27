import networkx as nx
from Node import NodeV
from helpers import add_node, add_edge, add_hyperedge, cut_edge, find_hanging_nodes, find_main_nodes


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
                    print(key, key1, value1, value2)
                    return False

    return True


def create_graph_6_with_mixed_edge_labels(labels=None):
    if labels is None:
        labels = [False, True, True, False, True, False]
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

    add_edge(G, v1, v2, labels[0])
    add_edge(G, v2, v3, labels[1])
    add_edge(G, v3, v4, labels[2])
    add_edge(G, v4, v5, labels[3])
    add_edge(G, v5, v6, labels[4])
    add_edge(G, v6, v1, labels[5])

    add_hyperedge(G, [v1, v2, v3, v4, v5, v6], True)

    return G


def get_node_inserting_func_for_test(graph, previous_node_id, divider, offset):
    previous_node = list(graph.nodes)[previous_node_id]
    following_node = list(graph.nodes)[(previous_node_id + 1) % divider]
    edge_to_break = list(graph.nodes)[previous_node_id + offset]
    return lambda: cut_edge(graph, previous_node, following_node, edge_to_break)


def add_hanging_nodes_to_graph_for_test(result_graph, edges):
    inserting_funcs = [get_node_inserting_func_for_test(result_graph, e, 6, 6) for e in edges]
    for f in inserting_funcs:
        new_node = f()
        new_node.h = True
        result_graph.nodes[new_node]['h'] = True
    return result_graph


def get_subgraph_inserting_func_for_test(graph, previous_node_id, index):
    previous_node = list(graph.nodes)[previous_node_id]
    following_node = list(graph.nodes)[(previous_node_id + 1) % 6]
    cutting_node = find_hanging_nodes(graph, find_main_nodes(graph))[index]
    new_node_coordinates = [(2, 1), (2, -1), (0, -2), (-2, -1), (-2, 1), (0, 2)]

    def f():
        x, y = new_node_coordinates[previous_node_id]
        new_node = NodeV(x, y, False)
        add_node(graph, new_node)
        add_edge(graph, previous_node, new_node, True)
        add_edge(graph, following_node, new_node, True)
        add_edge(graph, cutting_node, new_node, False)

    return f


def flip_x(arr):
    res = [(-x, y) for x, y in arr]
    res.reverse()
    return res


def flip_y(arr):
    res = [(x, -y) for x, y in arr]
    res.reverse()
    return res


def get_subgraph_inserting_func_for_test(graph, previous_node_id, index):
    previous_node = list(graph.nodes)[previous_node_id]
    following_node = list(graph.nodes)[(previous_node_id + 1) % 6]
    cutting_node = find_hanging_nodes(graph, find_main_nodes(graph))[index]
    new_nodes_coordinates = [[(1.5, 1.5), (2, 1), (2.5, 0.5)],
                             [(2.5, -0.5), (2, -1), (1.5, -1.5)],
                             [(1, -2), (0, -2), (-1, -2)]]
    new_nodes_coordinates += [flip_x(new_nodes_coordinates[1]), flip_x(new_nodes_coordinates[0]), flip_y(new_nodes_coordinates[2])]

    def f():
        v1 = NodeV(new_nodes_coordinates[previous_node_id][0][0], new_nodes_coordinates[previous_node_id][0][1], False)
        v2 = NodeV(new_nodes_coordinates[previous_node_id][1][0], new_nodes_coordinates[previous_node_id][1][1], False)
        v3 = NodeV(new_nodes_coordinates[previous_node_id][2][0], new_nodes_coordinates[previous_node_id][2][1], False)
        add_node(graph, v1)
        add_node(graph, v2)
        add_node(graph, v3)

        add_edge(graph, previous_node, v1, True)
        add_edge(graph, following_node, v3, True)
        add_edge(graph, v1, v2, True)
        add_edge(graph, v2, v3, True)
        add_edge(graph, cutting_node, v2, False)
        add_hyperedge(graph, [v1, v2, cutting_node, previous_node], False)
        add_hyperedge(graph, [v2, v3, following_node, cutting_node], False)

    return f


def add_subgraph_elements(result_graph, edges):
    inserting_funcs = [get_subgraph_inserting_func_for_test(result_graph, edges[i], i) for i in
                       range(len(edges))]
    for f in inserting_funcs:
        f()
    return result_graph


def create_graph_with_subgraph(hanging_node_ids):
    res = create_graph_6_with_mixed_edge_labels([i not in hanging_node_ids for i in range(6)])
    res = add_hanging_nodes_to_graph_for_test(res, hanging_node_ids)
    res = add_subgraph_elements(res, hanging_node_ids)
    return res
