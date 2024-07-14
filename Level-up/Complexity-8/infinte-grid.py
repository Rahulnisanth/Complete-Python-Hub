from collections import deque

def bfs(start_x, start_y, end_x, end_y):
    if (start_x, start_y) == (end_x, end_y):
        return 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    queue = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))
    while queue:
        x, y, steps = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) == (end_x, end_y):
                return steps + 1
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1

def find_minimum_steps(points):
    if not points: 
        return -1
    total = 0
    for i in range(1, len(points)):
        start_x, start_y = points[i - 1]
        end_x, end_y = points[i]
        steps = bfs(start_x, start_y, end_x, end_y)
        if steps == -1: 
            return -1
        else: 
            total += steps
    return total


# Input stream :
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print(find_minimum_steps(points))