# FIND IF PATH EXISTS :
import collections
def validPath(n: int, edges, start: int, destination: int) -> bool:
    graph = collections.defaultdict(list)
    # Dictionary for nearest nodes :
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # Depth-First Approach ->
    def dfs(node, visited):
        if node == destination:
            return True
        visited.add(node)
        for near in graph[node]:
            if near not in visited:
                if dfs(near, visited):
                    return True
        return False
    
    visited = set()
    return dfs(start, visited)