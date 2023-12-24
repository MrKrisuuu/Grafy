from group_6.productions_g6 import P13, P15, P14
from group_6.utils_g6 import create_graph_with_hanging_nodes
from utils import draw_graph
from start_graphs import *
from productions import *
from tests import do_tests


# G = test_start()
# draw_graph(G)
# P1.apply(G)
# draw_graph(G)
# P2.apply(G)
# draw_graph(G)
#
# print("P1")
# do_tests(get_P1_left, P1)
# print()
#
# print("P2")
# do_tests(get_P2_left, P2)
# print()
#
# G = create_graph_6()
# draw_graph(G)
# P(G, G)
# draw_graph(G)


if __name__ == '__main__':

    G = create_graph_with_hanging_nodes([2, 5])
    draw_graph(G)
    P13.apply(G)
    draw_graph(G)

    G = create_graph_with_hanging_nodes([2, 3, 4])
    draw_graph(G)
    P14.apply(G)
    draw_graph(G)


    G = create_graph_with_hanging_nodes([2, 3, 5])
    draw_graph(G)
    P15.apply(G)
    draw_graph(G)