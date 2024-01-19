from Node import NodeV, NodeE, NodeQ


def find_main_nodes(G):
    nodes = set()
    for edge in G.edges:
        if isinstance(edge[0], NodeQ):
            nodes.add(edge[1])
        if isinstance(edge[1], NodeQ):
            nodes.add(edge[0])
    return nodes


def find_hanging_nodes(G, main_nodes):
    nodes = []
    for node in G.nodes:
        if isinstance(node, NodeV) and node not in main_nodes:
            nodes.append(node)
    return nodes


def find_edges(G):
    edges = []
    for node in G.nodes:
        if isinstance(node, NodeE):
            edges.append(node)
    return edges


def find_nodes(G, e):
    nodes = []
    for edge in G.edges:
        if e in edge:
            if edge[0] == e:
                nodes.append(edge[1])
            else:
                nodes.append(edge[0])
    if len(nodes) != 2:
        print(nodes)
        raise Exception("Wrong!!!")
    return tuple(nodes)


def cut_edge(G, v1, v2, edge):
    G.remove_node(edge)
    new_v = NodeV(edge.x, edge.y, not edge.b)
    add_node(G, new_v)

    add_edge(G, new_v, v1, edge.b)
    add_edge(G, new_v, v2, edge.b)

    return new_v


def find_hyperedge(G):
    hyperedges = []
    for node in G.nodes:
        if isinstance(node, NodeQ):
            hyperedges.append(node)
    if len(hyperedges) != 1:
        print(hyperedges)
        raise Exception("Wrong!!!")
    return hyperedges[0]


def add_node(G, v):
    G.add_node(v, **v.__dict__)


def add_edge(G, v1, v2, b):
    edge = NodeE(v1, v2, b)
    add_node(G, edge)
    G.add_edge(edge, v1)
    G.add_edge(edge, v2)
    return edge


def add_hyperedge(G, nodes, r):
    hyperedge = NodeQ(nodes, r)
    add_node(G, hyperedge)
    for node in nodes:
        G.add_edge(hyperedge, node)
