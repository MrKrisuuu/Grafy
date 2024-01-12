from networkx.algorithms.isomorphism import ISMAGS, GraphMatcher

from group_6.utils_g6 import create_graph_with_hanging_nodes
from helpers import find_main_nodes, find_hanging_nodes, find_edges, find_nodes, cut_edge, find_hyperedge, add_node, add_edge, add_hyperedge
from start_graphs import *
from group_6.productions_g6 import P13, P14, P15

def P(G, subgraf):
    main_nodes = find_main_nodes(subgraf)
    hanging_nodes = find_hanging_nodes(subgraf, main_nodes)
    for node in hanging_nodes:
        G.nodes[node]["h"] = False
        node.h = False
    edges = find_edges(subgraf)
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

    q = find_hyperedge(subgraf)
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


class Production:
    def __init__(self, left):
        self.left = left

    def apply(self, graph):
        matcher = GraphMatcher(graph, self.left, node_match=node_match)
        for subgraph_nodes in matcher.subgraph_isomorphisms_iter():
            isomorphic_subgraph = graph.subgraph(subgraph_nodes)
            P(graph, isomorphic_subgraph)
            return True
        return False

class MarkProduction(Production):
    def __init__(self, left, mark_target_fun):
        super().__init__(left)
        self.mark_target_fun = mark_target_fun

    def apply(self, graph):
        matcher = GraphMatcher(graph, self.left, node_match=node_match)
        for subgraph_nodes in matcher.subgraph_isomorphisms_iter():
            isomorphic_subgraph = graph.subgraph(subgraph_nodes)
            return self.mark_target_fun(isomorphic_subgraph)
        return False


P1 = Production(get_P1_left())
P2 = Production(get_P2_left())
P3 = Production(get_P3_left())
P4 = Production(get_P4_left())
P7 = MarkProduction(get_P7_left(), mark_target_fun=mark_target_function)
P9 = Production(get_P9_left())
P10 = Production(get_P10_left())

P13 = Production(create_graph_with_hanging_nodes([2, 5]))
P14 = Production(create_graph_with_hanging_nodes([2, 3, 4]))
P15 = Production(create_graph_with_hanging_nodes([2, 3, 5]))

P21 = MarkProduction(get_P21_left(), mark_target_fun=mark_target_function)
