import pytest

from productions import P22
from start_graphs import get_P22_left
from tests import main_test, remove_vertex_test, remove_edge_test, change_r_test, add_node_test, b_false_test

P22_TESTS = (main_test, remove_vertex_test, remove_edge_test, change_r_test, add_node_test, b_false_test)

def test_P22():
    for test in P22_TESTS:
        assert test(get_P22_left, P22) == 1
