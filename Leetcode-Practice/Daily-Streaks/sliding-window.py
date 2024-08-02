# MINIMUM SWAPS TO GROUP ALL 1'S TOGETHER :
def minSwaps(nums) -> int:
    # Edge cases :
    ones = nums.count(1)
    if ones == 0 or ones == len(nums): 
        return 0
    # Main cases :
    nums = nums + nums
    N = len(nums)
    current_swaps = sum(1 for i in range(ones) if nums[i] == 0)
    minSwaps = current_swaps
    for i in range(ones, N):
        if nums[i] == 0:
            current_swaps += 1
        if nums[i - ones] == 0:
            current_swaps -= 1
        minSwaps = min(minSwaps, current_swaps)
    return minSwaps
