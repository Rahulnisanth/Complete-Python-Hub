#  CONTAINER WITH MOST WATER :
def mostWater(height) -> int:
    maxArea = 0
    start, bound = 0, len(height) - 1
    while start < bound:
        maxArea = max(maxArea, min(height[start], height[bound]) * (bound - start))
        if height[start] < height[bound]:
            start += 1
        else:
            bound -= 1
    return maxArea


# ARRAY ROTATION :
def rightRotater(arr, k) -> list[int]:
    def rotater(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    k %= len(arr)
    rotater(arr, 0, len(arr) - 1)
    rotater(arr, k, len(arr) - 1)
    rotater(arr, 0, k - 1)
    return arr
