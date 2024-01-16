from examples import create_flow_starting_graph
from group_3.productions_3 import P8
from productions import P7, P1, P2
from utils import draw_graph

if __name__ == '__main__':
    G = create_flow_starting_graph()

    def get_condition_checking_node_existence(nodes_to_check):
        def fun(nodes):
            epsilon = 1e-7
            cords = [(node.x, node.y) for node in nodes]
            for node in nodes_to_check:
                node_exists = len([n for n in cords if abs(n[0] - node[0]) < epsilon and abs(n[1] - node[1]) < epsilon])
                if not node_exists:
                    return False
            return True
        return fun

    P7.apply(G, get_condition_checking_node_existence([(3, 3), (3, 0)]))
    draw_graph(G)
    P1.apply(G)
    draw_graph(G)
    P7.apply(G, get_condition_checking_node_existence([(3, 3), (3, 1.5)]))
    draw_graph(G)
    P8.apply(G)
    draw_graph(G)
    P2.apply(G)
    draw_graph(G)
    P1.apply(G)
    draw_graph(G)
    P7.apply(G, get_condition_checking_node_existence([(3, 3), (3, 2.625)]))
    draw_graph(G)
    P8.apply(G)
    draw_graph(G)
    P2.apply(G)
    draw_graph(G)
    P1.apply(G)
    draw_graph(G)
