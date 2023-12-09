from group_5.graph6_breaker import break_graph_6_by_nodes
from productions import P11
from start_graphs import get_P11_left
from tests import *
import pytest

DEFAULT_TESTS_P11 = (main_test, remove_vertex_test, remove_edge_test, change_r_test, add_node_test, b_false_test)


def test_P11():
    for test in DEFAULT_TESTS_P11:
        assert 1 == test(get_P11_left, P11)


def test_isomorphism():
    p11 = P11
    left_side = break_graph_6_by_nodes(1, 2, 2, 3)
    assert 1 == main_test(get_left=lambda: left_side, P=p11)
