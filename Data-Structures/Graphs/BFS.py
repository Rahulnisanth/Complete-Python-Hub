from collections import deque, defaultdict

def bfs(node_count, edges):
    # creating graph :
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    # initializing starters :
    start_node = 0
    visited = set()
    queue = deque([start_node])
    result = []
    # traversing in bfs -->>
    # [visiting all the neighbor nodes one by one using queue DS at the time of removing the front-edge in queue] :
    while queue:
        current = queue.popleft()
        if current not in visited:
            result.append(current)
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result