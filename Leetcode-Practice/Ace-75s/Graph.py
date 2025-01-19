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


# NEAREST EXIT FROM ENTRANCE OF THE MAZE :
def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
  N, M = len(maze), len(maze[0])

  def isValid(i, j):
      return (0 <= i < N) and (0 <= j < M) and (maze[i][j] == ".")

  def isExit(i, j):
      return (i == 0 or i == N - 1 or j == 0 or j == M - 1) and [i, j] != entrance

  def bfs(startX, startY, visited):
      q = deque([(startX, startY, 0)])
      visited.add((startX, startY))
      while q:
          x, y, steps = q.popleft()
          if isExit(x, y):
              return steps
          for dirX, dirY in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
              newX, newY = x + dirX, y + dirY
              if isValid(newX, newY) and (newX, newY) not in visited:
                  q.append((newX, newY, steps + 1))
                  visited.add((newX, newY))
      return -1

  startX, startY = entrance
  visited = set()
  result = bfs(startX, startY, visited)
  return result if result > 0 else -1
