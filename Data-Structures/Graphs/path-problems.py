from collections import defaultdict, deque
import heapq

# FIND IF PATH EXISTS FROM SOURCE -> DESTINATION :
def is_path_available(graph, src, dest):
    visited = set()
    def dfs(v, visited):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    dfs(src, visited)
    return True if dest in visited else False


# FIND THE LENGTH OF THE SHORTEST PATH :
def shortest_path(V, graph, src, dest):
    distance = [-1] * (V + 1)
    distance[src] = 0
    q = deque([src])
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                q.append(neighbor)
                distance[neighbor] = distance[current] + 1
                if neighbor == dest:
                    return distance[dest]
    return distance[dest]


# FIND THE SHORTEST PATH IN THE WEIGHTED GRAPH USING DIJKSTRA'S ALGORITHM :
def dijkstra(V, graph, src, dest):
    distance = [float("inf")] * (V + 1)
    distance[src] = 0
    q = [(src, 0)]
    while q:
        current_node, current_weight = heapq.heappop(q)
        if current_weight > distance[current_node]:
            continue
        for v, w in graph[current_node]:
            d = current_weight + w
            if d < distance[v]:
                distance[v] = d
                heapq.heappush(q, (v, d))
    return distance[dest]


# MINIMUM FARM COST :
def min_farm_cost(n, d):
    d.sort()
    if n <= 2:
        return 0
    else:
        total_cost = 0
        for i in range(n // 2):
            total_cost += (d[n - i - 1] - d[i]) * (n - 2 * i - 1)
        total_cost -= (d[n - 1] - d[0])
        return total_cost
