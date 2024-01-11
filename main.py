from group_3.start_graphs_3 import get_P5_left, get_P6_left, get_P8_left
from group_3.productions_3 import P5, P6, P8
from group_3.tests import do_tests, get_generinc_tests, check_coordinates_test_P5, check_coordinates_test_P6, check_coordinates_test_P8
from utils import draw_graph

G = get_P5_left()
draw_graph(G)
P5.apply(G)
draw_graph(G)

print("P5")
do_tests(get_P5_left, P5, get_generinc_tests() + [check_coordinates_test_P5])
print()

G = get_P6_left()
draw_graph(G)
P6.apply(G)
draw_graph(G)

print("P6")
do_tests(get_P6_left, P6, get_generinc_tests() + [check_coordinates_test_P6])
print()

G = get_P8_left()
draw_graph(G)
P8.apply(G)
draw_graph(G)

print("P8")
do_tests(get_P8_left, P8, get_generinc_tests() + [check_coordinates_test_P8])
print()