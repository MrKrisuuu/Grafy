class NodeV:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
        self.type = "V"

    def __str__(self):
        return f"{self.type}\n{self.h}"


class NodeE:
    def __init__(self, v1, v2, b):
        self.x = (v1.x + v2.x) / 2
        self.y = (v1.y + v2.y) / 2
        self.b = b
        self.type = "E"

    def __str__(self):
        return f"{self.type}\n{self.b}"


class NodeQ:
    def __init__(self, nodes, r):
        x = 0
        y = 0
        for node in nodes:
            x += node.x
            y += node.y
        x /= len(nodes)
        y /= len(nodes)
        self.x = x
        self.y = y
        self.r = r
        self.type = "Q"

    def __str__(self):
        return f"{self.type}\n{self.r}"
