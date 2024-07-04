def paint_fill(grid, x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    if grid[x][y] != "0":
        return grid
    def backtrack(x, y):
        # Base case :
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "0":
            return
        # Dfs :
        else:
            grid[x][y] = "2"
            for dx, dy in directions:
                backtrack(x + dx, y + dy)
    backtrack(x, y)
    return grid

# Testers :
grid = [
    ["1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "1", "1"],
    ["1", "1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "1", "0"],
    ["1", "0", "1", "0", "1", "0"]
]
x, y = 2, 2
result = paint_fill(grid, x - 1, y - 1)
# Printing :
for row in result:
    print(' '.join(row))
