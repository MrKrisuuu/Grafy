from Node import NodeE, NodeV
from examples import create_graph_6
from group_6.productions_g6 import P13
from group_6.tests_utils import parse_nodes_data, compare_graph_elements, create_graph_6_with_subgraph, create_graph_6_with_mixed_labels, get_graph_with_hanging_nodes_for_test
from group_6.utils_g6 import create_graph_with_hanging_nodes
import random


EXPECTED_GRAPHS = {
    'simple_isomorphic_0': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}},
    'simple_isomorphic_1': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}},
    'simple_isomorphic_2': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}},
    'isomorphic_with_various_edge_labels': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': False, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': True, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': False, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': False, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': True, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': False, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': False, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}},
    'graph_with_subgraph_not_changed': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (2, 1): {'x': 2, 'y': 1, 'h': False, 'type': 'V'}, (2, 2): {'x': 2, 'y': 2, 'h': False, 'type': 'V'}, (-2, 2): {'x': -2, 'y': 2, 'h': False, 'type': 'V'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'b': True, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'b': True, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'b': True, 'type': 'E'}, (1.5, 1.0): {'x': 1.5, 'y': 1.0, 'b': False, 'type': 'E'}, (1.5, 1.5): {'x': 1.5, 'y': 1.5, 'b': False, 'type': 'E'}, (2.0, 1.5): {'x': 2.0, 'y': 1.5, 'b': False, 'type': 'E'}, (-1.5, 1.5): {'x': -1.5, 'y': 1.5, 'b': False, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'r': True, 'type': 'Q'}},
    'graph_with_subgraph_changed': {(1, 1): {'x': 1, 'y': 1, 'h': False, 'type': 'V'}, (1.5, 0): {'x': 1.5, 'y': 0, 'h': False, 'type': 'V'}, (1, -1): {'x': 1, 'y': -1, 'h': False, 'type': 'V'}, (-1, -1): {'x': -1, 'y': -1, 'h': False, 'type': 'V'}, (-1.5, 0): {'x': -1.5, 'y': 0, 'h': False, 'type': 'V'}, (-1, 1): {'x': -1, 'y': 1, 'h': False, 'type': 'V'}, (2, 1): {'x': 2, 'y': 1, 'h': False, 'type': 'V'}, (2, 2): {'x': 2, 'y': 2, 'h': False, 'type': 'V'}, (-2, 2): {'x': -2, 'y': 2, 'h': False, 'type': 'V'}, (1.5, 1.0): {'x': 1.5, 'y': 1.0, 'b': False, 'type': 'E'}, (1.5, 1.5): {'x': 1.5, 'y': 1.5, 'b': False, 'type': 'E'}, (2.0, 1.5): {'x': 2.0, 'y': 1.5, 'b': False, 'type': 'E'}, (-1.5, 1.5): {'x': -1.5, 'y': 1.5, 'b': False, 'type': 'E'}, (1.25, 0.5): {'x': 1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (1.125, 0.75): {'x': 1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (1.375, 0.25): {'x': 1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.25, -0.5): {'x': -1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (-1.125, -0.75): {'x': -1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (-1.375, -0.25): {'x': -1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.25, -0.5): {'x': 1.25, 'y': -0.5, 'h': False, 'type': 'V'}, (1.375, -0.25): {'x': 1.375, 'y': -0.25, 'b': True, 'type': 'E'}, (1.125, -0.75): {'x': 1.125, 'y': -0.75, 'b': True, 'type': 'E'}, (0.0, -1.0): {'x': 0.0, 'y': -1.0, 'h': False, 'type': 'V'}, (0.5, -1.0): {'x': 0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-0.5, -1.0): {'x': -0.5, 'y': -1.0, 'b': True, 'type': 'E'}, (-1.25, 0.5): {'x': -1.25, 'y': 0.5, 'h': False, 'type': 'V'}, (-1.375, 0.25): {'x': -1.375, 'y': 0.25, 'b': True, 'type': 'E'}, (-1.125, 0.75): {'x': -1.125, 'y': 0.75, 'b': True, 'type': 'E'}, (0.0, 1.0): {'x': 0.0, 'y': 1.0, 'h': False, 'type': 'V'}, (0.5, 1.0): {'x': 0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (-0.5, 1.0): {'x': -0.5, 'y': 1.0, 'b': True, 'type': 'E'}, (0.0, 0.0): {'x': 0.0, 'y': 0.0, 'h': False, 'type': 'V'}, (0.625, -0.25): {'x': 0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (0.0, -0.5): {'x': 0.0, 'y': -0.5, 'b': False, 'type': 'E'}, (-0.625, 0.25): {'x': -0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (0.0, 0.5): {'x': 0.0, 'y': 0.5, 'b': False, 'type': 'E'}, (0.625, 0.25): {'x': 0.625, 'y': 0.25, 'b': False, 'type': 'E'}, (-0.625, -0.25): {'x': -0.625, 'y': -0.25, 'b': False, 'type': 'E'}, (-0.5625, -0.625): {'x': -0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (-1.0, 0.0): {'x': -1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (-0.5625, 0.625): {'x': -0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}, (0.5625, -0.625): {'x': 0.5625, 'y': -0.625, 'r': False, 'type': 'Q'}, (1.0, 0.0): {'x': 1.0, 'y': 0.0, 'r': False, 'type': 'Q'}, (0.5625, 0.625): {'x': 0.5625, 'y': 0.625, 'r': False, 'type': 'Q'}},
}


def correct_graph_P13_test():
    for i in range(3):
        result_graph = create_graph_with_hanging_nodes([i, i + 3])
        is_changed = P13.apply(result_graph)
        result_graph_map = parse_nodes_data(result_graph.nodes.data())

        test_graph = EXPECTED_GRAPHS[f'simple_isomorphic_{i}']

        print("correct graph P13 test: edges: %2d, %2d" % (i, i + 3), compare_graph_elements(result_graph_map, test_graph))
        assert compare_graph_elements(result_graph_map, test_graph)
        assert is_changed


def correct_graph_P13_with_custom_graph_6_test():
    result_graph = create_graph_6_with_mixed_labels()
    result_graph = get_graph_with_hanging_nodes_for_test(result_graph, 6, 6, [2, 5])

    is_changed = P13.apply(result_graph)
    result_graph_map = parse_nodes_data(result_graph.nodes.data())

    print(result_graph_map)
    test_graph = EXPECTED_GRAPHS['isomorphic_with_various_edge_labels']

    test_result = compare_graph_elements(result_graph_map, test_graph)

    print("correct graph P13 test with custom graph 6: edges: %2d, %2d" % (2, 5), test_result)
    assert test_result
    assert is_changed


def remove_edge_P13_test():
    result_graph = create_graph_6()
    result_graph = get_graph_with_hanging_nodes_for_test(result_graph, 6, 6, [2, 5])
    edges = []

    for edge in result_graph.nodes:
        if isinstance(edge, NodeE):
            edges.append(edge)
    random_edge = random.choice(edges)
    result_graph.remove_node(random_edge)
    if not P13.apply(result_graph):
        print("remove edge test P13: ", True)
        assert True
    else:
        print("remove edge test P13: ", False)
        assert False


def remove_vertex_P13_test():
    result_graph = create_graph_6()
    result_graph = get_graph_with_hanging_nodes_for_test(result_graph, 6, 6, [2, 5])

    nodes = []
    for node in result_graph.nodes:
        if isinstance(node, NodeV):
            nodes.append(node)
    random_node = random.choice(nodes)
    result_graph.remove_node(random_node)
    if not P13.apply(result_graph):
        print("remove vertex test P13: ", True)
        assert True
    else:
        print("remove vertex test P13: ", False)
        assert False


def correct_graph_with_subgraph_with_no_hanging_nodes_P13_test():
    result_graph = create_graph_6_with_subgraph()
    is_changed = P13.apply(result_graph)
    result_graph_map = parse_nodes_data(result_graph.nodes.data())

    print(result_graph_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_not_changed']

    test_result = compare_graph_elements(result_graph_map, test_graph)

    print("correct graph with subgraph no hanging nodes P13 test: ", test_result)
    assert test_result
    assert not is_changed


def correct_graph_with_subgraph_with_hanging_nodes_P13_test():
    result_graph = create_graph_6_with_subgraph()
    result_graph = get_graph_with_hanging_nodes_for_test(result_graph, 10, 9, [0, 3])

    is_changed = P13.apply(result_graph)
    result_graph_map = parse_nodes_data(result_graph.nodes.data())

    print(result_graph_map)

    test_graph = EXPECTED_GRAPHS['graph_with_subgraph_changed']

    test_result = compare_graph_elements(result_graph_map, test_graph)

    print("correct graph with subgraph with hanging nodes P13 test: ", test_result)
    assert test_result
    assert is_changed


if __name__ == '__main__':
    correct_graph_P13_test()
    remove_edge_P13_test()
    remove_vertex_P13_test()
    correct_graph_P13_with_custom_graph_6_test()
    correct_graph_with_subgraph_with_no_hanging_nodes_P13_test()
    correct_graph_with_subgraph_with_hanging_nodes_P13_test()