from Node import NodeV
from tests import main_test, remove_vertex_test, remove_edge_test, change_r_test, add_node_test


def check_coordinates_test_P5(get_left, P):
    def doHaveSameCoordinates(G1, G2):
        nodes1 = list(filter(lambda x: isinstance(x, NodeV), G1.nodes))
        nodes2 = list(filter(lambda x: isinstance(x, NodeV), G2.nodes))
        for node1, node2 in zip(nodes1, nodes2[:-1]):
            if node1.x != node2.x or node1.y != node2.y:
                print(node1.x, node1.y, node2.x, node2.y)
                return False
        if not (nodes2[-1].x == 0.5 and nodes2[-1].y == 0.5):
            return False
        return True

    original_G = get_left()
    changed_G = get_left()
    if P.apply(changed_G) and doHaveSameCoordinates(original_G, changed_G):
        print(f"check_coordinates_test OK")
        return 1
    else:
        print(f"check_coordinates_test FAILED")
        return 0


def check_coordinates_test_P6(get_left, P):
    def doHaveSameCoordinates(G1, G2):
        nodes1 = list(filter(lambda x: isinstance(x, NodeV), G1.nodes))
        nodes2 = list(filter(lambda x: isinstance(x, NodeV), G2.nodes))
        for node1, node2 in zip(nodes1, nodes2[:-1]):
            if node1.x != node2.x or node1.y != node2.y:
                print(node1.x, node1.y, node2.x, node2.y)
                return False
        if not (nodes2[-1].x == 0.5 and nodes2[-1].y == 0.5):
            return False
        return True

    original_G = get_left()
    changed_G = get_left()
    if P.apply(changed_G) and doHaveSameCoordinates(original_G, changed_G):
        print(f"check_coordinates_test OK")
        return 1
    else:
        print(f"check_coordinates_test FAILED")
        return 0


def check_coordinates_test_P8(get_left, P):
    def doHaveSameCoordinates(G1, G2):
        for node1, node2 in zip(G1.nodes, G2.nodes):
            if node1.x != node2.x or node1.y != node2.y:
                return False
        return True

    original_G = get_left()
    changed_G = get_left()
    if P.apply(changed_G) and doHaveSameCoordinates(original_G, changed_G):
        print(f"check_coordinates_test OK")
        return 1
    else:
        print(f"check_coordinates_test FAILED")
        return 0


def get_generinc_tests():
    return [main_test, remove_vertex_test, remove_edge_test, change_r_test, add_node_test]
