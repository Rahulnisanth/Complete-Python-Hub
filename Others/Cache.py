def calculateOddSum(nums) -> int:
    left, right, total = 0, len(nums) - 1, 0
    while left <= right:
        if nums[left] % 2 != 0 :
            total += nums[left] 
        if nums[right] % 2 != 0:
            total += nums[right]
        left += 1
        right -= 1
    return total

n = int(input())
mapper = {}
for _ in range(n):
    count, num = list(map(int, input().split()))
    if num in mapper:
        mapper[num] += count
    else:
        mapper[num] = count

maxFreq = -1
minFreq = float('inf')
maxNum = None
minNum = None
for k, v in mapper.items():
    if v > maxFreq:
        maxFreq = v
        maxNum = k
    if v < minFreq:
        minFreq = v
        minNum = k

print(abs(maxNum - minNum))