def solve_grid(grid, N) -> int:
    red_positions = [-1] * N
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'R': red_positions[i] = j
    # Calculating the minimum moves :
    moves = 0
    for i in range(N):
        found = False
        for j in range(i, N):
            if red_positions[j] <= i:
                found = True
                for k in range(j, i, -1):
                    red_positions[k], red_positions[k - 1] = red_positions[k - 1], red_positions[k]
                    moves += 1
                break
        if not found:
            return -1
    return moves


# Input drive :
N = int(input())
grid = [list(input()) for _ in range(N)]
print(solve_grid(grid, N))

