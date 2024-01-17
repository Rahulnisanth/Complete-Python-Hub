#  CONTAINER WITH MOST WATER :
def mostWater(num) -> int:
    maxArea = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            maxArea = max(maxArea, min(num[i], num[j]) * (j - i))
    return maxArea
