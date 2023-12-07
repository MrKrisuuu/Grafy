from utils import draw_graph
from start_graphs import *
from productions import *


G = test_start()
draw_graph(G)
P1.apply(G)
draw_graph(G)
P2.apply(G)
draw_graph(G)