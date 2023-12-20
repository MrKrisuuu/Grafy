from utils import draw_graph
from start_graphs import *
from productions import *
from tests import do_tests


G = test_start()
draw_graph(G)
P1.apply(G)
draw_graph(G)
P2.apply(G)
draw_graph(G)

print("P1")
do_tests(get_P1_left, P1)
print()

print("P2")
do_tests(get_P2_left, P2)
print()

G = create_graph_6()
draw_graph(G)
P(G, G)
draw_graph(G)
