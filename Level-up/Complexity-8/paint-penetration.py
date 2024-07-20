def fillPaint(grid, x, y):
    # Checker for valid position :
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    # Depth first search implementation :
    def dfs(i, j, visited):
        visited.add((i, j))
        count =  1
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            nx, ny = x + i, y + j
            if is_valid(nx, ny) and (nx, ny) not in visited:
                if grid[nx][ny] == "0":
                    count += dfs(nx, ny, visited)
                visited.add((nx, ny))
        return count
    
    # Main drive :
    if grid[x][y] == "1": 
        return -1
    visited = set()
    result = dfs(x, y, visited)
    return result

# Input stream :
grid = eval(input())
x, y = list(map(int, input().split()))
print(fillPaint(grid, x - 1, y - 1))