# FIND THE NUMBER OF CONNECTED COMPONENTS IN THE GRAPH :
from collections import defaultdict, deque
def find_connected_components(graph, V):
    visited = set()
    count = 0
    for v in range(1, V + 1):
        if v not in visited:
            def dfs(v, visited):
                visited.add(v)
                for neighbor in graph[v]:
                    if neighbor not in visited:
                        dfs(neighbor, visited)
            dfs(v, visited)
            count += 1
    return count


# FIND THE LARGEST ISLAND COUNT IN THE GRAPH :
from collections import defaultdict, deque
def find_largest_island_count(graph, V):
    result = 0
    visited = set()
    for v in range(1, V + 1):
        if v not in visited:
            def helper(v, visited):
                q, node_count = deque([v]), 0
                while q:
                    current = q.popleft()
                    node_count += 1
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            q.append(neighbor)
                return node_count
            result = max(result, helper(v, visited))
    return result


# FIND WHETHER THE GRAPH IS STRONGLY CONNECTED OT NOT :
def is_strong_connected(graph, transposed_graph, V):
    # Checking the current graph :
    visited = set()
    def dfs(v, visited):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    dfs(0, visited)
    if any(v not in visited for v in range(V)):
        return False

    # Checking for transposed graph :
    visited = set()
    def dfs(v, visited):
        visited.add(v)
        for neighbor in transposed_graph[v]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    dfs(0, visited)
    if any(v not in visited for v in range(V)):
        return False

    return True


# Input drive :
V = int(input())
E = int(input())
graph = defaultdict(list)
transposed_graph = defaultdict(list)
for _ in range(E):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    transposed_graph[v].append(u)
print("YES" if is_strong_connected(graph, transposed_graph, V) else "NO")