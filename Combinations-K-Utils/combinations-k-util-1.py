def make_k_combinations(n, start, k, result, path):
    if k == 0:
        result.append(path[:)
        return 
    for i in range(start, n + 1):
        path.append(i)
        make_k_combinations(n, i + 1, k - 1, result, path)
        path.pop()

def make_combinations(n, k):
    result = []
    make_k_combinations(n, 0, k, result, [])
    return result

# Input Handlers
n = int(input())
k = int(input())
print(make_combinations(n, k))
