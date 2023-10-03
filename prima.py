from collections import defaultdict
import heapq


def prim(graph):
    start_vertex = list(graph.keys())[0]
    mst = set()
    visited = []
    heap = []
    heapq.heappush(heap, (0, None, start_vertex))

    while heap:
        weight, parent, vertex = heapq.heappop(heap)

        if vertex in visited:
            continue

        if parent is not None:
            mst.add((parent, vertex))

        visited.append(vertex)

        for neighbor, neighbor_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(heap, (neighbor_weight, vertex, neighbor))

    return mst


graph = {
    '0': [('1', 3), ('2', 1)],
    '1': [('0', 3), ('4', 4)],
    '2': [('0', 1), ('3', 2), ('6', 6)],
    '3': [('2', 2), ('6', 5), ('5', 8), ('4', 7)],
    '4': [('1', 4), ('5', 2), ('3', 7)],
    '5': [('4', 2), ('3', 8)],
    '6': [('3', 5), ('2', 6)]
}

print(prim(graph))
