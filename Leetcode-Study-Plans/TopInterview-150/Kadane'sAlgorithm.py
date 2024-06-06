# FIND THE MAXIMUM SUB-ARRAY IN A ARRAY :
def maxSubArray(nums) -> int:
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# FINDING THE MAXIMUM SUB-ARRAY IN CIRCULAR ARRAY :
def maxSubarraySumCircular(nums) -> int:
    total, currMaxx, currMin = 0, 0, 0
    maxx = float('-inf')
    minn = float('inf')

    for num in nums:
        total += num
        currMaxx = max(num, currMaxx + num)
        currMin = min(num, currMin + num)
        maxx = max(maxx, currMaxx)
        minn = min(minn, currMin)
        
    return maxx if maxx < 0 else max(maxx, total - minn)
    