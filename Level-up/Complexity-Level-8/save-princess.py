def is_safe(grid, x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] != 'X'

def modify_grid(grid, n, m):
    new_grid = [list(row) for row in grid]
    for i in range(1, n):
        if i % 2 == 0:
            new_grid[i] = grid[i][-1:] + grid[i][:-1]
        else:
            new_grid[i] = grid[i][1:] + grid[i][:1]
    return ["".join(row) for row in new_grid]

def backtrack(x, y, n, m, grid, memo, moves):
    # Base case:
    if x == n - 1 and y == m - 1:
        return moves
    # Memo storage for easy retrieval :
    memo.add((x, y, "".join(grid)))
    # Tracking Drivers :
    min_moves = float("inf")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
    new_grid = modify_grid(grid, n, m)
    # Traversing all the directions :
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if is_safe(new_grid, nx, ny) and (nx, ny, "".join(new_grid)) not in memo:
            dump_steps = backtrack(nx, ny, n, m, new_grid, memo, moves + 1)
            if dump_steps != float("inf"):
                min_moves = min(min_moves, dump_steps)
    memo.remove((x, y, "".join(grid)))
    return min_moves

# Input drive / Main drive :
n, m = list(map(int, input().split()))
grid = [input() for _ in range(n + 2)]
memo = set()
result = backtrack(0, 0, len(grid), len(grid[0]), grid, memo, 0)
print(result)



