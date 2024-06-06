result = []
def make_k_combinations(nums, n, k, idx, i, dump):
    if idx == k:
        if sum(list(dump)) == target:
            dump.sort() 
            if list(dump) not in result : result.append(list(dump)) 
        return 
    if i >= n: return 0
    dump[idx] = nums[i]
    # Including the num :
    make_k_combinations(nums, n, k, idx + 1, i + 1, dump)
    # Excluding the num :
    make_k_combinations(nums, n, k, idx, i + 1, dump)

def target_sum_make_combinations(nums, n):
    for k in range(n, 0, -1):
        dump = [0] * k
        make_k_combinations(nums, n, k, 0, 0, dump)
    return result if len(result) > 0 else "Empty"

# Input stream :
test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    print(target_sum_make_combinations(nums, n))