from heapq import heappop, heappush
from collections import defaultdict

def findTheCity(n, edges, distanceThreshold) -> int:
    # Building graph with edges :
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append([v, w])
        graph[v].append([u, w])
    # Visiting only the nodes within distance-threshold using BFS :
    def helper(start):
        q = [(0, start)]
        visited = set()
        while q:
            distance, current = heappop(q)
            if current not in visited:
                visited.add(current)
                for neighbor, weight in graph[current]:
                    overall_weight = distance + weight
                    if overall_weight <= distanceThreshold:
                        heappush(q, (overall_weight, neighbor))
        return len(visited) - 1
    # Core drive :
    min_count, result = n, None
    for city in range(n):
        min_neighbors_count = helper(city)
        if min_neighbors_count <= min_count:
            min_count = min_neighbors_count
            result = city
    return result
