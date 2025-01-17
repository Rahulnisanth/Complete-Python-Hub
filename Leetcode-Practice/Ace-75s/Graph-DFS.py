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
                    
        
