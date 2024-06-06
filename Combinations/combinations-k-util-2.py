result = []
def make_k_combinations(nums, n, k, idx, i, dump):
    if idx == k:
        result.append(list(dump)) 
        return 
    if i >= n: return 0
    dump[idx] = nums[i]
    # Including the num :
    make_k_combinations(nums, n, k, idx + 1, i + 1, dump)
    # Excluding the num :
    make_k_combinations(nums, n, k, idx, i + 1, dump)

def make_combinations(nums, k, n):
    dump = [0] * k
    make_k_combinations(nums, n, k, 0, 0, dump)
    return result

# Input stream :
nums = list(map(int, input().split()))
k = int(input())
print(make_combinations(nums, k, len(nums)))