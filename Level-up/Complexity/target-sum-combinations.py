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
    return result

# Input stream :
test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    answer = target_sum_make_combinations(nums, target)
    if len(answer) > 0:
        for i in range(len(answer)):
            print("(", end='')
            for j in range(len(answer[i])):
                print(f" {answer[i][j]}", end='')
            print(")", end='')
    else: print("Empty")