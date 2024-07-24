from collections import deque, defaultdict

def bfs(node_count, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    start_node = 0
    visited = set()
    queue = deque([start_node])
    result = []
    while queue:
        current = queue.popleft()
        if current not in visited:
            result.append(current)
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result