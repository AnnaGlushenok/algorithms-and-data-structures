class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        for v in vertices:
            self.parent[v] = v

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            self.parent[root1] = root2


def kruskal(graph):
    minimum_spanning_tree = set()
    edges = sorted(graph, key=lambda x: x[2])
    vertices = set()

    for edge in edges:
        v1, v2, _ = edge
        vertices.add(v1)
        vertices.add(v2)

    disjoint_set = DisjointSet(vertices)

    for edge in edges:
        v1, v2, _ = edge
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            disjoint_set.union(v1, v2)
            minimum_spanning_tree.add(edge)

    return minimum_spanning_tree


graph = [
    ('0', '1', 3),
    ('0', '2', 1),
    ('1', '4', 4),
    ('4', '5', 2),
    ('4', '3', 7),
    ('2', '3', 2),
    ('2', '6', 6),
    ('3', '6', 5),
    ('3', '5', 8)
]

minimum_spanning_tree = kruskal(graph)
print(minimum_spanning_tree)
