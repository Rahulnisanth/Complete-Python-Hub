from collections import deque
# CONTAIN VIRUS PROBLEM :
def containVirus(matrix):
    # Checker for valid position :
    def is_valid(x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
    
    # Breadth first search approach & finding the current infected, next infected and walls required :
    def bfs(i, j, visited):
        queue = deque([(i, j)])
        infected = set([(i, j)])
        next_infected = set()
        walls_needed = 0
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x + dx, y + dy
                if is_valid(newX, newY) and (newX, newY) not in visited:
                    if matrix[newX][newY] == 1:
                        infected.add((newX, newY))
                        queue.append((newX, newY))
                    elif matrix[newX][newY] == 0:
                        next_infected.add((newX, newY))
                        walls_needed += 1
                    visited.add((newX, newY))
        return infected, next_infected, walls_needed
    
    # Core logic drive :
    result = 1
    while True:
        regions = []
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    infected, next_infected, walls_needed = bfs(i, j, visited)
                    regions.append((infected, next_infected, walls_needed))
        # Running the loop until all regions are quarantined :
        if not regions: 
            break
        # Finding the region with more next infected region :
        regions.sort(key=lambda x : len(x[1]), reverse=True)
        large_infected, large_next_infected, large_walls_needed = regions[0]
        # If there is only one region :
        if not large_next_infected: 
            break
        # The more needed walls should be quarantined first :
        result += large_walls_needed
        # Quarantining the infected areas :
        for i, j in large_infected:
            matrix[i][j] = 2
        # Marking the surrounding cells of the next infected area as '1' [marking as infected]:
        for _infected, next_infected, _walls in regions[1:]:
            for i, j in next_infected:
                matrix[i][j] = 1
    return result * 2 if result == 2 else result


# Input stream :
grid = eval(input())
print(containVirus(grid))