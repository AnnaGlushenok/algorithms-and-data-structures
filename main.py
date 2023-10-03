from collections import deque


def wave_algorithm(graph, start_node, end_node):
    queue = deque()
    visited = set()
    distance = {}
    prev = {}

    queue.append(start_node)
    visited.add(start_node)
    distance[start_node] = 0
    prev[start_node] = None

    while queue:
        current_node = queue.popleft()

        if current_node == end_node:
            break

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                distance[neighbor] = distance[current_node] + 1
                prev[neighbor] = current_node

    if end_node not in distance:
        return None

    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()
    return path


maze = {
    'Enter': ['1', '8'],
    '1': ['Enter', '2'],
    '2': ['1', '3'],
    '3': ['2', '4', '11'],
    '4': ['3', '5'],
    '5': ['4', '11'],
    '6': ['7', '14'],
    '7': ['6', 'Exit'],
    '8': ['Enter', '9'],
    '9': ['8', '10'],
    '10': ['9'],
    '11': ['3', '5', '12', '14'],
    '12': ['11', '13'],
    '13': ['12', '14'],
    '14': ['6', '11', '13'],
    'Exit': ['7'],
}

start = 'Enter'
end = 'Exit'

result = wave_algorithm(maze, start, end)

if result:
    print("Путь найден:", result)
else:
    print("Путь не найден.")
