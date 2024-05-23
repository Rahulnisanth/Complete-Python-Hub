from collections import defaultdict

def dfs(node_count, edges):
    # creating graph :
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    # Sorting the edges :
    for node in graph:
        graph[node].sort()
    # initializing starters :
    start_node = 0
    visited = set()
    result = []
    # traversing in dfs -->>
    # [visiting all the neighbor nodes at once using recursion DS at the time of visiting a node] :
    def helper(node):
        if node not in visited:
            result.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    helper(neighbor)
    helper(start_node)
    return result