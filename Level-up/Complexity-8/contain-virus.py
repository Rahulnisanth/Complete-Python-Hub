from collections import deque
# CONTAIN VIRUS PROBLEM :
def containVirus(isInfected) -> int:
    N, M = len(isInfected), len(isInfected[0])

    def isValid(i, j):
        return (0 <= i < N) and (0 <= j < M)

    def bfs(i, j, visited):
        q = deque([(i, j)])
        infected = [(i, j)]
        next_infected = set()
        walls_needed = 0
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nextX, nextY = (x + dx), (y + dy)
                if isValid(nextX, nextY):
                    if isInfected[nextX][nextY] == 0:
                        next_infected.add((nextX, nextY))
                        walls_needed += 1
                    if (
                        isInfected[nextX][nextY] == 1
                        and (nextX, nextY) not in visited
                    ):
                        visited.add((nextX, nextY))
                        infected.append((nextX, nextY))
                        q.append((nextX, nextY))
        return [infected, next_infected, walls_needed]

    result = 0
    while True:
        regions = []
        visited = set()
        for i in range(N):
            for j in range(M):
                if isInfected[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    infected, next_infected, walls_needed = bfs(i, j, visited)
                    regions.append((infected, next_infected, walls_needed))
        if not regions:
            break
        regions.sort(key=lambda x: len(x[1]), reverse=True)
        large_infected, large_next_infected, large_walls_needed = regions[0]
        if not large_next_infected:
            break
        # Add the walls needed 
        result += large_walls_needed
        # Quarantine the current infected area
        for i, j in large_infected:
            isInfected[i][j] = 2
        # Spread the virus across next infected area to its neighbours cells all over the region
        for _, next_infected, _ in regions[1:]:
            for i, j in next_infected:
                if isInfected[i][j] == 0:
                    isInfected[i][j] = 1
    return result

# Input stream :
grid = eval(input())
print(containVirus(grid))
