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


# FIND MAXI DIAMETER AFTER MERGING TWO GRAPHS
class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        N, M = len(edges1) + 1, len(edges2) + 1
        adjList1 = self.buildAdjacencyList(N, edges1)
        adjList2 = self.buildAdjacencyList(M, edges2)
        diameter1 = self.findDiameter(N, adjList1)
        diameter2 = self.findDiameter(M, adjList2)
        combinedDiameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1
        return max(diameter1, diameter2, combinedDiameter)

    def buildAdjacencyList(self, size, edges):
        adjList = [[] for _ in range(size)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        return adjList

    def findDiameter(self, N, adjList):
        farthestNode, _ = self.findFarthestNode(N, adjList, 0)
        _, diameter = self.findFarthestNode(N, adjList, farthestNode)
        return diameter

    def findFarthestNode(self, N, adjList, node):
        q = deque([node])
        visited = [False] * N
        visited[node] = True
        maxDis, farthestNode = 0, node
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                farthestNode = curr
                for adj in adjList[curr]:
                    if not visited[adj]:
                        visited[adj] = True
                        q.append(adj)
            if q:
                maxDis += 1
        return farthestNode, maxDis

