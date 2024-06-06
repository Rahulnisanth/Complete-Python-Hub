result = []
def make_k_combinations(nums, n, k, idx, i, dump):
    if idx == k:
        if sum(dump) == target:
            print(dump)
        return 
    if i >= n: return 0
    dump[idx] = nums[i]
    # Including the num :
    make_k_combinations(nums, n, k, idx + 1, i + 1, dump)
    # Excluding the num :
    make_k_combinations(nums, n, k, idx, i + 1, dump)

def target_sum_make_combinations(nums):
    for k in range(1, len(nums) + 1):
        dump = [0] * k
        make_k_combinations(nums, len(nums), k, 0, 0, dump)
    return result


nums = list(map(int, input().split()))
target = int(input())
print(target_sum_make_combinations(nums))