def calculate_maximum_coins(nums, n):
    def game(start, end, nums):
        if start > end: return 0
        if start == end: return nums[start]
        take_start = nums[start] + min(game(start + 2, end, nums), game(start + 1, end - 1, nums))
        take_end = nums[end] + min(game(start + 1, end - 1, nums), game(start, end - 2, nums))
        return max(take_start, take_end)
        
    return game(0, n - 1, nums)


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    nums = list(map(int, input().split()))
    print(calculate_maximum_coins(nums, n))
