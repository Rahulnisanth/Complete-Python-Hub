# Finding the maximum rectangle in histogram :
def largest_rectangle(heights) -> int:
    area = float("-inf")
    for i in range(len(heights)):
        min_height = float("inf")
        for j in range(i, len(heights)):
            min_height = min(min_height, heights[j])
            area = max(area, (min_height * abs(j - i + 1)))
    return area

# Converting the rectangle -> histogram :
def find_max_area(grid) -> int:
    max_area = float("-inf")
    heights = [0] * (len(grid[0]))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        max_area = max(max_area, largest_rectangle(heights))
    return max_area

# Input stream :
n = int(input())
rectangle = [list(map(int, input().split())) for _ in range(n)]
print(find_max_area(rectangle))
