from group_3.start_graphs_3 import get_P5_left, get_P6_left
from productions_3 import P5, P6
from tests import do_tests
from utils import draw_graph

G = get_P5_left()
draw_graph(G)
P5.apply(G)
draw_graph(G)

print("P5")
do_tests(get_P5_left, P5)
print()

G = get_P6_left()
draw_graph(G)
P6.apply(G)
draw_graph(G)

print("P6")
do_tests(get_P6_left, P6)
print()
