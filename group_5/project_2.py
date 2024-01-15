import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

from examples import create_flow_starting_graph
from group_3.productions_3 import P6, P8
from productions import P21, P9, P7, P2, P3, P1, node_match
from utils import draw_graph
from copy import deepcopy, copy

def node_match_by_Q(n1, n2):
    if len(n1) == 0:
        raise Exception("Set the dict!")

    if len(n2) == 0:
        raise Exception("Set the dict!")

    if n1["type"] != n2["type"]:
        return False

    if n1["type"] == "Q":
        return n1["x"] == n2["x"] and n1["y"] == n2["y"]

    return True

G = create_flow_starting_graph()
# draw_graph(G)

P21.apply(G)
# draw_graph(G)

P9.apply(G)
# draw_graph(G)

P7.apply(G)
# draw_graph(G)

P8.apply(G)
# draw_graph(G)

P8.apply(G)
# draw_graph(G)

P2.apply(G)
# draw_graph(G)

P3.apply(G)
# draw_graph(G)

_, subgraph = P1.apply(G)
# draw_graph(G)

for i in range(20):
    temp_G = deepcopy(G)
    matcher = GraphMatcher(temp_G, subgraph, node_match=node_match)
    nodes_dict = list(matcher.subgraph_isomorphisms_iter())

    subgraph_nodes = nodes_dict[0]
    isomorphic_subgraph = temp_G.subgraph(subgraph_nodes)
    counter = 0
    _, correct_subgraph = P7.apply(isomorphic_subgraph)
    # draw_graph(temp_G)
    for i in range(3):
        if P8.apply(temp_G):
            counter+=1
            if counter == 1:
                prev = deepcopy(temp_G)
    if counter == 2:
        # draw_graph(prev)
        # draw_graph(temp_G)
        G = temp_G
        break


P2.apply(G)
# draw_graph(G)

P3.apply(G)
# draw_graph(G)

P1.apply(G)
# draw_graph(G)



