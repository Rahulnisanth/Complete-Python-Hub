def rob(nums):
    def rob_linear(nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prev1, prev2 = 0, 0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        return prev1
    n = len(nums)
    if n == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Input stream :
amounts = list(map(int, input().split(",")))
print(rob(amounts)) 
