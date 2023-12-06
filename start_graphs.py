from examples import create_graph_4, create_graph_6
from helpers import cut_edge


def get_P1():
    G = create_graph_4()
    return G


def get_P2():
    G = create_graph_4()
    v1 = list(G.nodes)[0]
    v2 = list(G.nodes)[1]
    e = list(G.nodes)[4]
    v = cut_edge(G, v1, v2, e)
    v.h = True
    return G