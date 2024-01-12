from examples import create_graph_6
from helpers import cut_edge


def get_node_inserting_func(graph, previous_node_id):
    previous_node = list(graph.nodes)[previous_node_id]
    following_node = list(graph.nodes)[(previous_node_id + 1) % 6]
    edge_to_break = list(graph.nodes)[previous_node_id + 6]
    return lambda: cut_edge(graph, previous_node, following_node, edge_to_break)


def create_graph_with_hanging_nodes(edges_to_break):
    graph = create_graph_6()
    inserting_funcs = [get_node_inserting_func(graph, e) for e in edges_to_break]
    for f in inserting_funcs:
        new_node = f()
        new_node.h = True
        graph.nodes[new_node]['h'] = True
    return graph
