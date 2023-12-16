from group_6.productions import P13
from group_6.utils import create_graph_with_hanging_nodes
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

if __name__ == '__main__':
    # TODO restore it after manual testing
    G = create_graph_with_hanging_nodes([2, 5])
    draw_graph(G)
    P13.apply(G)
    draw_graph(G)
