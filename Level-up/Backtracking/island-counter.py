# Back-tracker :
def backtrack(i, j, grid):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
        grid[i][j] = 0 
        solution[i][j] = "#"
        backtrack(i + 1, j, grid) # Down
        backtrack(i, j + 1, grid) # Right
        backtrack(i - 1, j, grid) # Up
        backtrack(i, j - 1, grid) # Left

# Traversing each island :
def find_island_count(grid):
    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island_count += 1
                backtrack(i, j, grid)
    return island_count

# Input Stream :
row, col = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(row)]

# Solution grid :
solution = [[0] * (len(grid[0])) for _ in range(len(grid))]
# Solution :
print(find_island_count(grid))
# Printing the solution grid :
for row in solution:
    print(row)
