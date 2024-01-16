from examples import create_flow_starting_graph
from group_3.productions_3 import P8
from helpers import find_edges
from productions import P7, P1, P2, MarkProduction
from start_graphs import get_P7_left, mark_target_function
from utils import draw_graph
from functools import cmp_to_key


def compare_edges(e1, e2):
    if e1.x == e2.x:
        return e2.y - e1.y
    return e2.x - e1.x


def mark_top_right_edge(G):
    edges = find_edges(G)
    edges.sort(key=cmp_to_key(compare_edges))
    edges[0].marked = True
    G.nodes[edges[0]]["marked"] = True


class P1_2:
    def apply(self, G):
        applied = P1.apply(G)
        if applied:
            mark_top_right_edge(G)
        return applied


if __name__ == '__main__':
    left_side = get_P7_left()
    mark_top_right_edge(left_side)
    P7_2 = MarkProduction(left_side, mark_target_fun=mark_target_function)
    P1_2 = P1_2()
    G = create_flow_starting_graph()
    mark_top_right_edge(G)
    P7_2.apply(G)
    draw_graph(G)
    P1_2.apply(G)
    draw_graph(G)
    P7_2.apply(G)
    draw_graph(G)
    P8.apply(G)
    draw_graph(G)
    P2.apply(G)
    draw_graph(G)
    P1_2.apply(G)
    draw_graph(G)
    P7_2.apply(G)
    draw_graph(G)
    P8.apply(G)
    draw_graph(G)
    P2.apply(G)
    draw_graph(G)
    P1_2.apply(G)
    draw_graph(G)
