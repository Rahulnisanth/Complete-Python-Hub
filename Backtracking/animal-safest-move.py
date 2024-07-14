# Storage fields :
stack = []
min_steps = float("inf")

# Valid position checker :
def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

# Marking the unsafe paths as 8 for easy backtracking:
def mark_unsafe_paths(grid, power, n, m):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 8
                for p in range(1, power + 1):
                    if is_valid(i, j + p, n, m): grid[i][j + p] = 8
                    if is_valid(i, j - p, n, m): grid[i][j - p] = 8
                    if is_valid(i + p, j, n, m): grid[i + p][j] = 8
                    if is_valid(i - p, j, n, m): grid[i - p][j] = 8
                    if is_valid(i + p, j + p, n, m): grid[i + p][j + p] = 8
                    if is_valid(i - p, j - p, n, m): grid[i - p][j - p] = 8
                    if is_valid(i - p, j + p, n, m): grid[i - p][j + p] = 8
                    if is_valid(i + p, j - p, n, m): grid[i + p][j - p] = 8
    return grid

# Backtracking to find the shortest path from left to right
def backtrack(i, j, n, m, grid, solution, steps):
    global min_steps, stack
    if j == m - 1:
        solution[i][j] = 1
        vertices.append((i + 1, j + 1))
        if steps < min_steps:
            min_steps = steps
            stack = vertices.copy()
        vertices.pop()
        return False
    if is_valid(i, j, n, m) and grid[i][j] != 8 and solution[i][j] != 1 and steps < min_steps:
        solution[i][j] = 1
        vertices.append((i + 1, j + 1))
        if backtrack(i , j + 1, n, m, grid, solution, steps + 1): return True
        if backtrack(i + 1, j, n, m, grid, solution, steps + 1): return True
        if backtrack(i, j - 1, n, m, grid, solution, steps + 1): return True
        if backtrack(i - 1, j, n, m, grid, solution, steps + 1): return True
        vertices.pop()
        solution[i][j] = 0
    return False

# Input stream:
n = int(input())
m = int(input())
power = int(input())
grid = [list(map(int, input().split(", "))) for i in range(n)]

# Initialize the solution grid and vertices list
solution = [[0] * m for _ in range(n)]
vertices = []

# After marking the blocked vertices:
result = mark_unsafe_paths(grid, power, n, m)
for row in result:
    print(row)

# Backtracking for the shortest path:
for i in range(n):
    if result[i][0] != 8:
        if backtrack(i, 0, n, m, result, solution, 0): break
        else: continue

print("Final Vertices :")
print(stack)
print(min_steps)    


'''
0, 1, 1, 1, 0, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 1, 1, 0, 1
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 0, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
1, 0, 1, 1, 1, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 1, 1, 1, 0
1, 1, 1, 1, 1, 0, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
'''