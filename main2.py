def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    while priority_queue:
        priority_queue = sorted(priority_queue, key=lambda x: x[0])
        current_distance, current_vertex = priority_queue.pop(0)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[str(current_vertex)].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))

    return distances


graph = {
    '0': {'1': 3, '2': 1},
    '1': {'0': 3, '4': 4},
    '2': {'0': 1, '6': 6, '3': 2},
    '3': {'2': 2, '6': 5, '5': 8, '4': 7},
    '4': {'1': 4, '5': 2, '3': 7},
    '5': {'3': 8, '4': 2},
    '6': {'2': 6, '3': 5}
}
print(dijkstra(graph, 0))
