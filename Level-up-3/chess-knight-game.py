def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def get_possible_moves(x, y, n):
    moves = []
    for dx, dy in [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]:
        newX, newY = x + dx, y + dy
        if is_valid(newX, newY, n):
            moves.append((newX, newY))
    return moves

def get_minimum_steps(n, startX, startY, endX, endY):
    queue = [(startX, startY)]
    visited = set()
    visited.add((startX, startY))
    steps = 0
    
    while queue:
        next_queue = []
        for currentX, currentY in queue:
            if currentX == endX and currentY == endY:
                return steps
            for newX, newY in get_possible_moves(currentX, currentY, n):
                if (newX, newY) not in visited:
                    next_queue.append((newX, newY))
                    visited.add((newX, newY))
        queue = next_queue
        steps += 1
    
    return -1

n = 8
x = int(input())
y = int(input())
u = int(input())
v = int(input())
result = get_minimum_steps(n, x-1, y-1,u-1,v-1)
print(result if result != -1 else -1)
