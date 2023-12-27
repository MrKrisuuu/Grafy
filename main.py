from utils import draw_graph
from start_graphs import *
from productions import *
from tests import do_tests, DEFAULT_MARK_TESTS


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

G = get_P9_left()
draw_graph(G)
P9.apply(G)
draw_graph(G)

G = get_P3_left()
draw_graph(G)
P3.apply(G)
draw_graph(G)

print("P3")
do_tests(get_P3_left, P3)
print()

G = get_P4_left()
draw_graph(G)
P4.apply(G)
draw_graph(G)

print("P4")
do_tests(get_P4_left, P4)
print()

G = get_P7_left()
draw_graph(G)
P7.apply(G)
draw_graph(G)

print("P7")
do_tests(get_P7_left, P7, tests=DEFAULT_MARK_TESTS)
print()


print("P9")
do_tests(get_P9_left, P9)
print()

G = get_P10_left()
draw_graph(G)
P10.apply(G)
draw_graph(G)

print("P10")
do_tests(get_P10_left, P10)
print()
