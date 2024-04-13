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
