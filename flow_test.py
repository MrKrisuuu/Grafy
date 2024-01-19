from examples import create_flow_starting_graph
from group_3.productions_3 import P8
from productions import *
from utils import draw_graph
import numpy as np


def get_hyperedge_at(graph, x, y):
    h_edges = [h_edge for h_edge in graph.nodes if isinstance(h_edge, NodeQ)]
    distances = [(h_edge.x - x) ** 2 + (h_edge.y - y) ** 2 for h_edge in h_edges]

    return h_edges[np.argmin(distances)]

G = create_flow_starting_graph()

P7.apply(G, node_q=get_hyperedge_at(G, 2, 1))
draw_graph(G)
P1.apply(G)
draw_graph(G)
P7.apply(G, node_q=get_hyperedge_at(G, 1.6, 1.1))
draw_graph(G)
P8.apply(G)
draw_graph(G)
P22.apply(G, node_q=get_hyperedge_at(G, 0.0, 0.0))
draw_graph(G)
P2.apply(G)
draw_graph(G)
P11.apply(G)
draw_graph(G)
P1.apply(G)
draw_graph(G)
P7.apply(G, node_q=get_hyperedge_at(G, 1.3, 1.1))
draw_graph(G)
P8.apply(G)
draw_graph(G)
P8.apply(G)
draw_graph(G)
P2.apply(G)
draw_graph(G)
P3.apply(G)
draw_graph(G)
P1.apply(G)
draw_graph(G)
#edges = get_hyperedges(G)
#print(edges)

