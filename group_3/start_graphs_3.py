from examples import create_graph_4
from helpers import cut_edge


def get_P5_left():
    G = create_graph_4()

    v3 = list(G.nodes)[0]
    v2 = list(G.nodes)[1]
    v1 = list(G.nodes)[2]
    v4 = list(G.nodes)[3]

    e23 = list(G.nodes)[4]
    e12 = list(G.nodes)[5]
    e14 = list(G.nodes)[6]
    e43 = list(G.nodes)[7]

    def f(ve1, ve2, ee12):
        v = cut_edge(G, ve1, ve2, ee12)
        v.h = True
        G.nodes[v]['h'] = True

    # e43.b = False
    # G.nodes[e43]['b'] = False
    f(v3, v2, e23)
    f(v1, v2, e12)
    f(v1, v4, e14)

    return G


def get_P6_left():
    G = create_graph_4()
    v3 = list(G.nodes)[0]
    v2 = list(G.nodes)[1]
    v1 = list(G.nodes)[2]
    v4 = list(G.nodes)[3]

    e23 = list(G.nodes)[4]
    e12 = list(G.nodes)[5]
    e14 = list(G.nodes)[6]
    e43 = list(G.nodes)[7]

    def f(ve1, ve2, ee12):
        v = cut_edge(G, ve1, ve2, ee12)
        v.h = True
        G.nodes[v]['h'] = True

    f(v3, v2, e23)
    f(v1, v2, e12)
    f(v1, v4, e14)
    f(v4, v3, e43)

    return G
