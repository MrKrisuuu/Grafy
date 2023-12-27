from Node import NodeE, NodeV
from examples import create_graph_6
from group_6.productions_g6 import P13, P14, P15
from group_6.tests_utils import parse_nodes_data, compare_graph_elements, \
    create_graph_6_with_mixed_edge_labels, add_hanging_nodes_to_graph_for_test, \
    create_graph_with_subgraph
from group_6.utils_g6 import create_graph_with_hanging_nodes
import random

from utils import draw_graph

EXPECTED_GRAPHS = {
    'simple_result': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}},
    'isomorphic_with_various_edge_labels_P13_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': True, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}},
    'graph_with_subgraph_not_changed_P13_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'r': True, 'type': 'Q'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': True, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': True, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (1.5, 1.5): {'x': 1.5, 'y': 1.5, 'h': False, 'type': 'V'}, (2, 1): {'x': 2, 'y': 1, 'h': False, 'type': 'V'}, (2.5, 0.5): {'x': 2.5, 'y': 0.5, 'h': False, 'type': 'V'}, (1.25, 1.25): {'x': 1.25, 'y': 1.25, 'b': True, 'type': 'E'}, (2.0, 0.25): {'x': 2.0, 'y': 0.25, 'b': True, 'type': 'E'}, (1.75, 1.25): {'x': 1.75, 'y': 1.25, 'b': True, 'type': 'E'}, (2.25, 0.75): {'x': 2.25, 'y': 0.75, 'b': True, 'type': 'E'}, (1.625, 0.75): {'x': 1.625, 'y': 0.75, 'b': False, 'type': 'E'}, (1.4375, 1.0): {'x': 1.4375, 'y': 1.0, 'r': False, 'type': 'Q'}, (1.8125, 0.5): {'x': 1.8125, 'y': 0.5, 'r': False, 'type': 'Q'}, (2.5, -0.5): {'x': 2.5, 'y': -0.5, 'h': False, 'type': 'V'}, (2, -1): {'x': 2, 'y': -1, 'h': False, 'type': 'V'}, (1.5, -1.5): {'x': 1.5, 'y': -1.5, 'h': False, 'type': 'V'}, (2.0, -0.25): {'x': 2.0, 'y': -0.25, 'b': True, 'type': 'E'}, (1.25, -1.25): {'x': 1.25, 'y': -1.25, 'b': True, 'type': 'E'}, (2.25, -0.75): {'x': 2.25, 'y': -0.75, 'b': True, 'type': 'E'}, (1.75, -1.25): {'x': 1.75, 'y': -1.25, 'b': True, 'type': 'E'}, (1.625, -0.75): {'x': 1.625, 'y': -0.75, 'b': False, 'type': 'E'}, (1.8125, -0.5): {'x': 1.8125, 'y': -0.5, 'r': False, 'type': 'Q'}, (1.4375, -1.0): {'x': 1.4375, 'y': -1.0, 'r': False, 'type': 'Q'}, (-1.5, -1.5): {'x': -1.5, 'y': -1.5, 'h': False, 'type': 'V'}, (-2, -1): {'x': -2, 'y': -1, 'h': False, 'type': 'V'}, (-2.5, -0.5): {'x': -2.5, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.25, -1.25): {'x': -1.25, 'y': -1.25, 'b': True, 'type': 'E'}, (-2.0, -0.25): {'x': -2.0, 'y': -0.25, 'b': True, 'type': 'E'}, (-1.75, -1.25): {'x': -1.75, 'y': -1.25, 'b': True, 'type': 'E'}, (-2.25, -0.75): {'x': -2.25, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.625, -0.75): {'x': -1.625, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.4375, -1.0): {'x': -1.4375, 'y': -1.0, 'r': False, 'type': 'Q'}, (-1.8125, -0.5): {'x': -1.8125, 'y': -0.5, 'r': False, 'type': 'Q'}},
    'graph_with_subgraph_changed_P13_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (1, -2): {'x': 1, 'y': -2, 'h': False, 'type': 'V'}, (0, -2): {'x': 0, 'y': -2, 'h': False, 'type': 'V'}, (-1, -2): {'x': -1, 'y': -2, 'h': False, 'type': 'V'}, (1.0, -1.5): {'x': 1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (-1.0, -1.5): {'x': -1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (0.5, -2.0): {'x': 0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (-0.5, -2.0): {'x': -0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (0.0, -1.5): {'x': 0.0, 'y': -1.5, 'b': False, 'type': 'E'}, (0.5, -1.5): {'x': 0.5, 'y': -1.5, 'r': False, 'type': 'Q'}, (-0.5, -1.5): {'x': -0.5, 'y': -1.5, 'r': False, 'type': 'Q'}, (-1, 2): {'x': -1, 'y': 2, 'h': False, 'type': 'V'}, (0, 2): {'x': 0, 'y': 2, 'h': False, 'type': 'V'}, (1, 2): {'x': 1, 'y': 2, 'h': False, 'type': 'V'}, (-1.0, 1.5): {'x': -1.0, 'y': 1.5, 'b': True, 'type': 'E'}, (1.0, 1.5): {'x': 1.0, 'y': 1.5, 'b': True, 'type': 'E'}, (-0.5, 2.0): {'x': -0.5, 'y': 2.0, 'b': True, 'type': 'E'}, (0.5, 2.0): {'x': 0.5, 'y': 2.0, 'b': True, 'type': 'E'}, (0.0, 1.5): {'x': 0.0, 'y': 1.5, 'b': False, 'type': 'E'}, (-0.5, 1.5): {'x': -0.5, 'y': 1.5, 'r': False, 'type': 'Q'}, (0.5, 1.5): {'x': 0.5, 'y': 1.5, 'r': False, 'type': 'Q'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}},
    'isomorphic_with_various_edge_labels_P14_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': True, 'type': 'V'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}},
    'graph_with_subgraph_not_changed_P14_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'r': True, 'type': 'Q'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': True, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.5, 1.5): {'x': 1.5, 'y': 1.5, 'h': False, 'type': 'V'}, (2, 1): {'x': 2, 'y': 1, 'h': False, 'type': 'V'}, (2.5, 0.5): {'x': 2.5, 'y': 0.5, 'h': False, 'type': 'V'}, (1.25, 1.25): {'x': 1.25, 'y': 1.25, 'b': True, 'type': 'E'}, (2.0, 0.25): {'x': 2.0, 'y': 0.25, 'b': True, 'type': 'E'}, (1.75, 1.25): {'x': 1.75, 'y': 1.25, 'b': True, 'type': 'E'}, (2.25, 0.75): {'x': 2.25, 'y': 0.75, 'b': True, 'type': 'E'}, (1.625, 0.75): {'x': 1.625, 'y': 0.75, 'b': False, 'type': 'E'}, (1.4375, 1.0): {'x': 1.4375, 'y': 1.0, 'r': False, 'type': 'Q'}, (1.8125, 0.5): {'x': 1.8125, 'y': 0.5, 'r': False, 'type': 'Q'}, (1, -2): {'x': 1, 'y': -2, 'h': False, 'type': 'V'}, (0, -2): {'x': 0, 'y': -2, 'h': False, 'type': 'V'}, (-1, -2): {'x': -1, 'y': -2, 'h': False, 'type': 'V'}, (1.0, -1.5): {'x': 1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (-1.0, -1.5): {'x': -1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (0.5, -2.0): {'x': 0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (-0.5, -2.0): {'x': -0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (0.0, -1.5): {'x': 0.0, 'y': -1.5, 'b': False, 'type': 'E'}, (0.5, -1.5): {'x': 0.5, 'y': -1.5, 'r': False, 'type': 'Q'}, (-0.5, -1.5): {'x': -0.5, 'y': -1.5, 'r': False, 'type': 'Q'}, (-2.5, 0.5): {'x': -2.5, 'y': 0.5, 'h': False, 'type': 'V'}, (-2, 1): {'x': -2, 'y': 1, 'h': False, 'type': 'V'}, (-1.5, 1.5): {'x': -1.5, 'y': 1.5, 'h': False, 'type': 'V'}, (-2.0, 0.25): {'x': -2.0, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.25, 1.25): {'x': -1.25, 'y': 1.25, 'b': True, 'type': 'E'}, (-2.25, 0.75): {'x': -2.25, 'y': 0.75, 'b': True, 'type': 'E'}, (-1.75, 1.25): {'x': -1.75, 'y': 1.25, 'b': True, 'type': 'E'}, (-1.625, 0.75): {'x': -1.625, 'y': 0.75, 'b': False, 'type': 'E'}, (-1.8125, 0.5): {'x': -1.8125, 'y': 0.5, 'r': False, 'type': 'Q'}, (-1.4375, 1.0): {'x': -1.4375, 'y': 1.0, 'r': False, 'type': 'Q'}},
    'graph_with_subgraph_changed_P14_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (1.5, 1.5): {'x': 1.5, 'y': 1.5, 'h': False, 'type': 'V'}, (2, 1): {'x': 2, 'y': 1, 'h': False, 'type': 'V'}, (2.5, 0.5): {'x': 2.5, 'y': 0.5, 'h': False, 'type': 'V'}, (1.25, 1.25): {'x': 1.25, 'y': 1.25, 'b': True, 'type': 'E'}, (2.0, 0.25): {'x': 2.0, 'y': 0.25, 'b': True, 'type': 'E'}, (1.75, 1.25): {'x': 1.75, 'y': 1.25, 'b': True, 'type': 'E'}, (2.25, 0.75): {'x': 2.25, 'y': 0.75, 'b': True, 'type': 'E'}, (1.625, 0.75): {'x': 1.625, 'y': 0.75, 'b': False, 'type': 'E'}, (1.4375, 1.0): {'x': 1.4375, 'y': 1.0, 'r': False, 'type': 'Q'}, (1.8125, 0.5): {'x': 1.8125, 'y': 0.5, 'r': False, 'type': 'Q'}, (2.5, -0.5): {'x': 2.5, 'y': -0.5, 'h': False, 'type': 'V'}, (2, -1): {'x': 2, 'y': -1, 'h': False, 'type': 'V'}, (1.5, -1.5): {'x': 1.5, 'y': -1.5, 'h': False, 'type': 'V'}, (2.0, -0.25): {'x': 2.0, 'y': -0.25, 'b': True, 'type': 'E'}, (1.25, -1.25): {'x': 1.25, 'y': -1.25, 'b': True, 'type': 'E'}, (2.25, -0.75): {'x': 2.25, 'y': -0.75, 'b': True, 'type': 'E'}, (1.75, -1.25): {'x': 1.75, 'y': -1.25, 'b': True, 'type': 'E'}, (1.625, -0.75): {'x': 1.625, 'y': -0.75, 'b': False, 'type': 'E'}, (1.8125, -0.5): {'x': 1.8125, 'y': -0.5, 'r': False, 'type': 'Q'}, (1.4375, -1.0): {'x': 1.4375, 'y': -1.0, 'r': False, 'type': 'Q'}, (1, -2): {'x': 1, 'y': -2, 'h': False, 'type': 'V'}, (0, -2): {'x': 0, 'y': -2, 'h': False, 'type': 'V'}, (-1, -2): {'x': -1, 'y': -2, 'h': False, 'type': 'V'}, (1.0, -1.5): {'x': 1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (-1.0, -1.5): {'x': -1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (0.5, -2.0): {'x': 0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (-0.5, -2.0): {'x': -0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (0.0, -1.5): {'x': 0.0, 'y': -1.5, 'b': False, 'type': 'E'}, (0.5, -1.5): {'x': 0.5, 'y': -1.5, 'r': False, 'type': 'Q'}, (-0.5, -1.5): {'x': -0.5, 'y': -1.5, 'r': False, 'type': 'Q'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}},
    'isomorphic_with_various_edge_labels_P15_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}},
    'graph_with_subgraph_not_changed_P15_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'r': True, 'type': 'Q'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': True, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': True, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': False, 'type': 'E'}, (1.5, 1.5): {'x': 1.5, 'y': 1.5, 'h': False, 'type': 'V'}, (2, 1): {'x': 2, 'y': 1, 'h': False, 'type': 'V'}, (2.5, 0.5): {'x': 2.5, 'y': 0.5, 'h': False, 'type': 'V'}, (1.25, 1.25): {'x': 1.25, 'y': 1.25, 'b': True, 'type': 'E'}, (2.0, 0.25): {'x': 2.0, 'y': 0.25, 'b': True, 'type': 'E'}, (1.75, 1.25): {'x': 1.75, 'y': 1.25, 'b': True, 'type': 'E'}, (2.25, 0.75): {'x': 2.25, 'y': 0.75, 'b': True, 'type': 'E'}, (1.625, 0.75): {'x': 1.625, 'y': 0.75, 'b': False, 'type': 'E'}, (1.4375, 1.0): {'x': 1.4375, 'y': 1.0, 'r': False, 'type': 'Q'}, (1.8125, 0.5): {'x': 1.8125, 'y': 0.5, 'r': False, 'type': 'Q'}, (2.5, -0.5): {'x': 2.5, 'y': -0.5, 'h': False, 'type': 'V'}, (2, -1): {'x': 2, 'y': -1, 'h': False, 'type': 'V'}, (1.5, -1.5): {'x': 1.5, 'y': -1.5, 'h': False, 'type': 'V'}, (2.0, -0.25): {'x': 2.0, 'y': -0.25, 'b': True, 'type': 'E'}, (1.25, -1.25): {'x': 1.25, 'y': -1.25, 'b': True, 'type': 'E'}, (2.25, -0.75): {'x': 2.25, 'y': -0.75, 'b': True, 'type': 'E'}, (1.75, -1.25): {'x': 1.75, 'y': -1.25, 'b': True, 'type': 'E'}, (1.625, -0.75): {'x': 1.625, 'y': -0.75, 'b': False, 'type': 'E'}, (1.8125, -0.5): {'x': 1.8125, 'y': -0.5, 'r': False, 'type': 'Q'}, (1.4375, -1.0): {'x': 1.4375, 'y': -1.0, 'r': False, 'type': 'Q'}, (1, -2): {'x': 1, 'y': -2, 'h': False, 'type': 'V'}, (0, -2): {'x': 0, 'y': -2, 'h': False, 'type': 'V'}, (-1, -2): {'x': -1, 'y': -2, 'h': False, 'type': 'V'}, (1.0, -1.5): {'x': 1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (-1.0, -1.5): {'x': -1.0, 'y': -1.5, 'b': True, 'type': 'E'}, (0.5, -2.0): {'x': 0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (-0.5, -2.0): {'x': -0.5, 'y': -2.0, 'b': True, 'type': 'E'}, (0.0, -1.5): {'x': 0.0, 'y': -1.5, 'b': False, 'type': 'E'}, (0.5, -1.5): {'x': 0.5, 'y': -1.5, 'r': False, 'type': 'Q'}, (-0.5, -1.5): {'x': -0.5, 'y': -1.5, 'r': False, 'type': 'Q'}},
    'graph_with_subgraph_changed_P15_test': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (1.5, 1.5): {'x': 1.5, 'y': 1.5, 'h': False, 'type': 'V'}, (2, 1): {'x': 2, 'y': 1, 'h': False, 'type': 'V'}, (2.5, 0.5): {'x': 2.5, 'y': 0.5, 'h': False, 'type': 'V'}, (1.25, 1.25): {'x': 1.25, 'y': 1.25, 'b': True, 'type': 'E'}, (2.0, 0.25): {'x': 2.0, 'y': 0.25, 'b': True, 'type': 'E'}, (1.75, 1.25): {'x': 1.75, 'y': 1.25, 'b': True, 'type': 'E'}, (2.25, 0.75): {'x': 2.25, 'y': 0.75, 'b': True, 'type': 'E'}, (1.625, 0.75): {'x': 1.625, 'y': 0.75, 'b': False, 'type': 'E'}, (1.4375, 1.0): {'x': 1.4375, 'y': 1.0, 'r': False, 'type': 'Q'}, (1.8125, 0.5): {'x': 1.8125, 'y': 0.5, 'r': False, 'type': 'Q'}, (2.5, -0.5): {'x': 2.5, 'y': -0.5, 'h': False, 'type': 'V'}, (2, -1): {'x': 2, 'y': -1, 'h': False, 'type': 'V'}, (1.5, -1.5): {'x': 1.5, 'y': -1.5, 'h': False, 'type': 'V'}, (2.0, -0.25): {'x': 2.0, 'y': -0.25, 'b': True, 'type': 'E'}, (1.25, -1.25): {'x': 1.25, 'y': -1.25, 'b': True, 'type': 'E'}, (2.25, -0.75): {'x': 2.25, 'y': -0.75, 'b': True, 'type': 'E'}, (1.75, -1.25): {'x': 1.75, 'y': -1.25, 'b': True, 'type': 'E'}, (1.625, -0.75): {'x': 1.625, 'y': -0.75, 'b': False, 'type': 'E'}, (1.8125, -0.5): {'x': 1.8125, 'y': -0.5, 'r': False, 'type': 'Q'}, (1.4375, -1.0): {'x': 1.4375, 'y': -1.0, 'r': False, 'type': 'Q'}, (-1.5, -1.5): {'x': -1.5, 'y': -1.5, 'h': False, 'type': 'V'}, (-2, -1): {'x': -2, 'y': -1, 'h': False, 'type': 'V'}, (-2.5, -0.5): {'x': -2.5, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.25, -1.25): {'x': -1.25, 'y': -1.25, 'b': True, 'type': 'E'}, (-2.0, -0.25): {'x': -2.0, 'y': -0.25, 'b': True, 'type': 'E'}, (-1.75, -1.25): {'x': -1.75, 'y': -1.25, 'b': True, 'type': 'E'}, (-2.25, -0.75): {'x': -2.25, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.625, -0.75): {'x': -1.625, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.4375, -1.0): {'x': -1.4375, 'y': -1.0, 'r': False, 'type': 'Q'}, (-1.8125, -0.5): {'x': -1.8125, 'y': -0.5, 'r': False, 'type': 'Q'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}}
}


def correct_graph_P13_test(draw_graphs):
    for i in range(3):
        left_side = create_graph_with_hanging_nodes([i, i + 3])
        is_changed = apply_test(left_side, draw_graphs, P13)
        left_side_map = parse_nodes_data(left_side.nodes.data())

        test_graph = EXPECTED_GRAPHS['simple_result']

        print("correct graph P13 test: edges: %2d, %2d" % (i, i + 3), compare_graph_elements(left_side_map, test_graph))
        assert compare_graph_elements(left_side_map, test_graph)
        assert is_changed


def correct_graph_P13_with_custom_graph_6_test(draw_graphs):
    left_side = create_graph_6_with_mixed_edge_labels()
    left_side = add_hanging_nodes_to_graph_for_test(left_side,[2, 5])

    is_changed = apply_test(left_side, draw_graphs, P13)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)
    test_graph = EXPECTED_GRAPHS['isomorphic_with_various_edge_labels_P13_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("correct graph P13 test with custom graph 6: edges: %2d, %2d" % (2, 5), test_result)
    assert test_result
    assert is_changed


def remove_edge_P13_test(draw_graphs):
    left_side = create_graph_6()
    left_side = add_hanging_nodes_to_graph_for_test(left_side,[2, 5])
    edges = []

    for edge in left_side.nodes:
        if isinstance(edge, NodeE):
            edges.append(edge)
    random_edge = random.choice(edges)
    left_side.remove_node(random_edge)

    success = not apply_test(left_side, draw_graphs, P13)

    print("remove edge test P13: ", success)
    assert success


def remove_vertex_P13_test(draw_graphs):
    left_side = create_graph_6()
    left_side = add_hanging_nodes_to_graph_for_test(left_side, [2, 5])

    nodes = []
    for node in left_side.nodes:
        if isinstance(node, NodeV):
            nodes.append(node)
    random_node = random.choice(nodes)
    left_side.remove_node(random_node)

    success = not apply_test(left_side, draw_graphs, P13)
    print("remove vertex test P13: ", success)
    assert success


def incorrect_graph_with_subgraph_with_hanging_nodes_P13_test(draw_graphs):
    left_side = create_graph_with_subgraph([0, 1, 3])
    is_changed = apply_test(left_side, draw_graphs, P13)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_not_changed_P13_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("incorrect graph with subgraph with hanging nodes P13 test: ", test_result)
    assert test_result
    assert not is_changed


def correct_graph_with_subgraph_with_hanging_nodes_P13_test(draw_graphs):
    left_side = create_graph_with_subgraph([2, 5])

    is_changed = apply_test(left_side, draw_graphs, P13)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_changed_P13_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("correct graph with subgraph with hanging nodes P13 test: ", test_result)
    assert test_result
    assert is_changed


# P14

def correct_graph_P14_test(draw_graphs):
    for i in range(3):
        left_side = create_graph_with_hanging_nodes([i, i + 1, i + 2])
        is_changed = apply_test(left_side, draw_graphs, P14)
        left_side_map = parse_nodes_data(left_side.nodes.data())

        test_graph = EXPECTED_GRAPHS['simple_result']

        print("correct graph P14 test: edges: %2d, %2d, %2d" % (i, i + 1, i + 2), compare_graph_elements(left_side_map, test_graph))
        assert compare_graph_elements(left_side_map, test_graph)
        assert is_changed


def correct_graph_P14_with_custom_graph_6_test(draw_graphs):
    left_side = create_graph_6_with_mixed_edge_labels()
    left_side = add_hanging_nodes_to_graph_for_test(left_side, [2, 3, 4])

    is_changed = apply_test(left_side, draw_graphs, P14)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)
    test_graph = EXPECTED_GRAPHS['isomorphic_with_various_edge_labels_P14_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("correct graph P14 test with custom graph 6: edges: %2d, %2d, %2d" % (2, 3, 4), test_result)
    assert test_result
    assert is_changed


def remove_edge_P14_test(draw_graphs):
    left_side = create_graph_6()
    left_side = add_hanging_nodes_to_graph_for_test(left_side, [2, 3, 4])
    edges = []

    for edge in left_side.nodes:
        if isinstance(edge, NodeE):
            edges.append(edge)
    random_edge = random.choice(edges)
    left_side.remove_node(random_edge)

    success = not apply_test(left_side, draw_graphs, P14)

    print("remove edge test P14: ", success)
    assert success


def remove_vertex_P14_test(draw_graphs):
    left_side = create_graph_6()
    left_side = add_hanging_nodes_to_graph_for_test(left_side, [2, 3, 4])

    nodes = []
    for node in left_side.nodes:
        if isinstance(node, NodeV):
            nodes.append(node)
    random_node = random.choice(nodes)
    left_side.remove_node(random_node)

    success = not apply_test(left_side, draw_graphs, P14)
    print("remove vertex test P14: ", success)
    assert success


def incorrect_graph_with_subgraph_with_hanging_nodes_P14_test(draw_graphs):
    left_side = create_graph_with_subgraph([0, 2, 4])

    is_changed = apply_test(left_side, draw_graphs, P14)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_not_changed_P14_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("incorrect graph with subgraph with hanging nodes P14 test: ", test_result)
    assert test_result
    assert not is_changed


def correct_graph_with_subgraph_with_hanging_nodes_P14_test(draw_graphs):
    left_side = create_graph_with_subgraph([0, 1, 2])

    is_changed = apply_test(left_side, draw_graphs, P14)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_changed_P14_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("correct graph with subgraph with hanging nodes P14 test: ", test_result)
    assert test_result
    assert is_changed


# P15
def correct_graph_P15_test(draw_graphs):
    for i in range(6):
        left_side = create_graph_with_hanging_nodes([i, (i + 1) % 6, (i + 3) % 6])
        is_changed = apply_test(left_side, draw_graphs, P15)
        left_side_map = parse_nodes_data(left_side.nodes.data())

        print(left_side_map)

        test_graph = EXPECTED_GRAPHS['simple_result']

        print("correct graph P15 test: edges: %2d, %2d, %d" % (i, (i + 1) % 6, (i + 3) % 6), compare_graph_elements(left_side_map, test_graph))
        assert compare_graph_elements(left_side_map, test_graph)
        assert is_changed


def correct_graph_P15_with_custom_graph_6_test(draw_graphs):
    left_side = create_graph_6_with_mixed_edge_labels()
    left_side = add_hanging_nodes_to_graph_for_test(left_side, [2, 3, 5])

    is_changed = apply_test(left_side, draw_graphs, P15)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)
    test_graph = EXPECTED_GRAPHS['isomorphic_with_various_edge_labels_P15_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("correct graph P15 test with custom graph 6: edges: %2d, %2d, %2d" % (2, 3, 5), test_result)
    assert test_result
    assert is_changed


def remove_edge_P15_test(draw_graphs):
    left_side = create_graph_6()
    left_side = add_hanging_nodes_to_graph_for_test(left_side, [2, 3, 5])
    edges = []

    for edge in left_side.nodes:
        if isinstance(edge, NodeE):
            edges.append(edge)
    random_edge = random.choice(edges)
    left_side.remove_node(random_edge)

    success = not apply_test(left_side, draw_graphs, P15)

    print("remove edge test P15: ", success)
    assert success


def remove_vertex_P15_test(draw_graphs):
    left_side = create_graph_6()
    left_side = add_hanging_nodes_to_graph_for_test(left_side, [2, 3, 5])

    nodes = []
    for node in left_side.nodes:
        if isinstance(node, NodeV):
            nodes.append(node)
    random_node = random.choice(nodes)
    left_side.remove_node(random_node)

    success = not apply_test(left_side, draw_graphs, P15)
    print("remove vertex test P15: ", success)
    assert success


def incorrect_graph_with_subgraph_with_hanging_nodes_P15_test(draw_graphs):
    left_side = create_graph_with_subgraph([0, 1, 2])

    is_changed = apply_test(left_side, draw_graphs, P15)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_not_changed_P15_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("incorrect graph with subgraph with hanging nodes P15 test: ", test_result)
    assert test_result
    assert not is_changed


def correct_graph_with_subgraph_with_hanging_nodes_P15_test(draw_graphs):
    left_side = create_graph_with_subgraph([0, 1, 3])

    is_changed = apply_test(left_side, draw_graphs, P15)
    left_side_map = parse_nodes_data(left_side.nodes.data())

    print(left_side_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_changed_P15_test']

    test_result = compare_graph_elements(left_side_map, test_graph)

    print("correct graph with subgraph with hanging nodes P15 test: ", test_result)
    assert test_result
    assert is_changed


def apply_test(graph, draw, production):
    if draw:
        draw_graph(graph)

    is_changed = production.apply(graph)

    if draw:
        draw_graph(graph)

    return is_changed


if __name__ == '__main__':
    DRAW_GRAPHS = False
    # P13
    correct_graph_P13_test(DRAW_GRAPHS)
    remove_edge_P13_test(DRAW_GRAPHS)
    remove_vertex_P13_test(DRAW_GRAPHS)
    correct_graph_P13_with_custom_graph_6_test(DRAW_GRAPHS)
    incorrect_graph_with_subgraph_with_hanging_nodes_P13_test(DRAW_GRAPHS)
    correct_graph_with_subgraph_with_hanging_nodes_P13_test(DRAW_GRAPHS)

    # P14
    correct_graph_P14_test(DRAW_GRAPHS)
    remove_edge_P14_test(DRAW_GRAPHS)
    remove_vertex_P14_test(DRAW_GRAPHS)
    correct_graph_P14_with_custom_graph_6_test(DRAW_GRAPHS)
    incorrect_graph_with_subgraph_with_hanging_nodes_P14_test(DRAW_GRAPHS)
    correct_graph_with_subgraph_with_hanging_nodes_P14_test(DRAW_GRAPHS)

    # P15
    correct_graph_P15_test(DRAW_GRAPHS)
    remove_edge_P15_test(DRAW_GRAPHS)
    remove_vertex_P15_test(DRAW_GRAPHS)
    correct_graph_P15_with_custom_graph_6_test(DRAW_GRAPHS)
    incorrect_graph_with_subgraph_with_hanging_nodes_P15_test(DRAW_GRAPHS)
    correct_graph_with_subgraph_with_hanging_nodes_P15_test(DRAW_GRAPHS)
