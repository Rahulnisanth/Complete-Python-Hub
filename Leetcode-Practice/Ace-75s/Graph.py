# KEYS AND ROOMS :
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
      N = len(rooms)
      visited = [False] * N
      visited[0] = True
      stack = [0]
      while stack:
          current_node = stack.pop()
          for neighbour in rooms[current_node]:   
              if not visited[neighbour]:
                  visited[neighbour] = True
                  stack.append(neighbour)
      return all(visited)
                    

# NUMBER OF PROVINCES :
def findCircleNum(self, isConnected: List[List[int]]) -> int:
  def bfs(node, isConnected, visited):
      q = deque([node])
      visited[node] = True
      while q:
          current_node = q.popleft()
          for i in range(len(isConnected)):
              if isConnected[current_node][i] == 1 and not visited[i]:
                  q.append(i)
                  visited[i] = True

  N = len(isConnected)
  visited = [False] * N
  result = 0
  for i in range(N):
      if not visited[i]:
          result += 1
          bfs(i, isConnected, visited)
  return result


# REORDER ROUTES TO MAKE ALL PATHS LEAD TO ZERO :
def minReorder(self, n: int, connections: List[List[int]]) -> int:
  adjacencyMatrix = self.buildAdjacencyMatrix(connections, n)
  visited = [False] * n

  def bfs(node, count):
      q = deque([node])
      visited[node] = True
      while q:
          current = q.popleft()
          for neighbour, outgoing in adjacencyMatrix[current]:
              if not visited[neighbour]:
                  visited[neighbour] = True
                  if outgoing:
                      count += 1
                  q.append(neighbour)
      return count

  return bfs(0, 0)

def buildAdjacencyMatrix(self, graph, n):
  matrix = [[] for _ in range(n)]
  for a, b in graph:
      matrix[a].append((b, True))
      matrix[b].append((a, False))
  return matrix
