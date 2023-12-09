import pytest

from group_5.graph6_breaker import break_graph_6_by_nodes
from productions import P12
from start_graphs import get_P12_left
from tests import *
from helpers import add_node, add_edge

DEFAULT_TESTS_P12 = (main_test, remove_vertex_test, remove_edge_test, change_r_test, add_node_test, b_false_test)


def test_P12():
    for test in DEFAULT_TESTS_P12:
        test(get_P12_left, P12)


def test_isomorphism():
    p12 = P12
    left_side = break_graph_6_by_nodes(1, 2, 3, 4)
    assert 1 == main_test(get_left=lambda: left_side, P=p12)
