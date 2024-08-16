# MAXIMAL RECTANGLE :
def maximalRectangle(matrix) -> int:
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    else:
        row, col = len(matrix), len(matrix[0])
        heights = [0] * col
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, largestArea(heights))
        return maxArea

def largestArea(heights):
    stack, n = [], len(heights)
    maxArea = 0
    for i in range(n + 1):
        h = 0 if i == n else heights[i]
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        stack.append(i)
    return maxArea


# FIND THE SAFEST PATH IN GRID :
from collections import deque
import heapq
def maximumSafenessFactor(grid) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visits = [[float('inf')] * n for _ in range(n)]
        queue = deque()

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    visits[row][col] = 0

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n and visits[nr][nc] == float('inf'):
                    visits[nr][nc] = visits[row][col] + 1
                    queue.append((nr, nc))

        max_heap = [(-visits[0][0], 0, 0)]
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = visits[0][0]

        while max_heap:
            d, row, col = heapq.heappop(max_heap)
            d = -d
            if row == n - 1 and col == n - 1:
                return d  

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_safe = min(d, visits[nr][nc])
                    if new_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safe
                        heapq.heappush(max_heap, (-new_safe, nr, nc))
        return -1  


# COUNT THE EQUAL ROW AND COLUMN PAIRS :
def equalPairs(grid) -> int:
    if not grid:
        return 0
    def helper(grid, row, col):
        row_list = grid[row]
        col_list = [grid[i][col] for i in range(len(grid))]
        return row_list, col_list
    # Main drive...
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            row_list, col_list = helper(grid, i, j)
            if row_list == col_list:
                count += 1
    return count