from Node import NodeQ
from examples import create_flow_starting_graph
from productions import P1, P10, P2, P3, P7, MarkProduction
from start_graphs import get_P7_left, mark_target_function
from utils import draw_graph


def find_q_index_node_by_coords(G, x, y):
    index = 0
    for q in list(filter(lambda node: isinstance(node, NodeQ), G.nodes)):
        if q.x == x and q.y == y:
            return index
        index += 1


# Step 1
G = create_flow_starting_graph()
draw_graph(G)

# Step 2
P7 = MarkProduction(G, mark_target_fun=lambda left: mark_target_function(left, 1))
P7.apply(G)
draw_graph(G)

# Step 3
P1.apply(G)
draw_graph(G)

# Step 4
Qx = 1.59375
Qy = 1.125
q_index = find_q_index_node_by_coords(G, Qx, Qy)
P7 = MarkProduction(G, mark_target_fun=lambda left: mark_target_function(left, q_index))
P7.apply(G)
draw_graph(G)


# Step 5
P8 = MarkProduction(G, mark_target_fun=lambda left: mark_target_function(left, 0))
P8.apply(G)

P22 = MarkProduction(G, mark_target_fun=lambda left: mark_target_function(left, 5))
P22.apply(G)
draw_graph(G)

# Step 6
P10.apply(G)
draw_graph(G)

# Step 7
P3.apply(G)
draw_graph(G)

# Step 8
P1.apply(G)
draw_graph(G)


# Step 9
Qx = 1.3046875
Qy = 1.09375
q_index = find_q_index_node_by_coords(G, Qx, Qy)
P7 = MarkProduction(G, mark_target_fun=lambda left: mark_target_function(left, q_index))
P7.apply(G)
draw_graph(G)

# Step 10
Qx = 0.5625
Qy = 0.625
q_index = find_q_index_node_by_coords(G, Qx, Qy)
P8 = MarkProduction(G, mark_target_fun=lambda left: mark_target_function(left, q_index))
P8.apply(G)

Qx = 0.75
Qy = 1.5
q_index = find_q_index_node_by_coords(G, Qx, Qy)
P8 = MarkProduction(G, mark_target_fun=lambda left: mark_target_function(left, q_index))
P8.apply(G)
draw_graph(G)

# Step 11
P2.apply(G)
draw_graph(G)

# Step 12
P3.apply(G)
draw_graph(G)

# Step 13
P1.apply(G)

draw_graph(G)
