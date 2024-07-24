from collections import defaultdict

def dfs(node_count, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    for node in graph:
        graph[node].sort()

    visited = set()
    result = []
    def helper(node):
        result.append(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                helper(neighbor)
    helper(0)
    return result


# DETECT CYCLE IN THE GRAPH :
def helper(array, nodes):
    graph = defaultdict(list)
    for u,v in array:
        graph[u].append(v)
    
    # Core cycle detection function :
    def detect_cycle(node, visited, stack):
        visited.add(node)
        stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if detect_cycle(neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False

    visited = set()
    stack = set()
    for node in range(nodes):
        if node not in visited:
            if detect_cycle(node, visited, stack):
                return "true"
    return "false"


