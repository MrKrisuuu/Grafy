from examples import create_graph_6
from helpers import cut_edge


def break_graph_6_by_nodes(v1, v2, v3, v4):
    G = create_graph_6()

    first_v = list(G.nodes)[v1-1]
    second_v = list(G.nodes)[v2-1]
    third_v = list(G.nodes)[v3-1]
    fourth_v = list(G.nodes)[v4-1]

    first_e = list(G.nodes)[5+v1]
    second_e = list(G.nodes)[5+v3]

    first_second_v = cut_edge(G, first_v, second_v, first_e)
    third_fourth_v = cut_edge(G, third_v, fourth_v, second_e)

    first_second_v.h = True
    G.nodes[first_second_v]['h'] = True

    third_fourth_v.h = True
    G.nodes[third_fourth_v]['h'] = True

    return G