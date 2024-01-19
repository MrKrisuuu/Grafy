from networkx.algorithms.isomorphism import GraphMatcher

from Node import NodeQ
from group_3.start_graphs_3 import get_P6_left, get_P5_left, get_P8_left
from productions import Production, node_match_p7
from productions import node_match

P5 = Production(get_P5_left())
P6 = Production(get_P6_left())


class P8(Production):
    def __init__(self):
        super().__init__(get_P8_left())

    def apply(self, graph, node_q=None):
        matcher = GraphMatcher(graph, self.left, node_match=node_match_p7)
        for subgraph_nodes in matcher.subgraph_isomorphisms_iter():
            isomorphic_subgraph = graph.subgraph(subgraph_nodes)
            if node_q and node_q not in isomorphic_subgraph.nodes:
                continue
            for node in isomorphic_subgraph.nodes:
                if isinstance(node, NodeQ):
                    graph.nodes[node]["r"] = True
                    node.r = True
            return True
        return False


P8 = P8()
