def target_sum_make_combinations(nums, target):
    result, dump = [], []
    nums.sort()
    def helper(idx, remain):
        if remain == 0:
            dump.sort()
            if dump[:] not in result and sum(dump[:]) == target: 
                result.append(dump[:])
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]: continue
            if nums[i] > remain: break
            dump.append(nums[i])
            helper(idx + 1, remain - nums[i])
            dump.pop()
    helper(0, target)
    return result if len(result) > 0 else "Empty"

# Input stream :
test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    print(target_sum_make_combinations(nums, target))