from examples import create_flow_starting_graph
from group_3.productions_3 import P8
from helpers import find_edges
from productions import P1, P2, MarkProduction
from start_graphs import get_P7_left, mark_target_function
from utils import draw_graph


if __name__ == '__main__':
    left_side = get_P7_left()
    e = find_edges(left_side)[0]
    left_side.nodes[e]["marked"] = True
    e.marked = True
    P7_2 = MarkProduction(left_side, mark_target_fun=mark_target_function)
    G = create_flow_starting_graph()

    P7_2.apply(G)
    draw_graph(G)
    P1.apply(G)
    draw_graph(G)
    P7_2.apply(G)
    draw_graph(G)
    P8.apply(G)
    draw_graph(G)
    P2.apply(G)
    draw_graph(G)
    P1.apply(G)
    draw_graph(G)
    P7_2.apply(G)
    draw_graph(G)
    P8.apply(G)
    draw_graph(G)
    P2.apply(G)
    draw_graph(G)
    P1.apply(G)
    draw_graph(G)
