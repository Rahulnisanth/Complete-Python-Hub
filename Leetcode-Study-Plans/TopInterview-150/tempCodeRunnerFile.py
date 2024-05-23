
# SUBSETS :
def subsets(nums):
    def backtrack(nums, index = 0, subset = []):
        result.append(list(subset))
        for i in range(index, len(nums)):
            subset.append(nums[i])
            backtrack(nums, i + 1, subset)
            subset.pop()
    result = []
    backtrack(nums)
    return result

print(subsets([1,2,3]))