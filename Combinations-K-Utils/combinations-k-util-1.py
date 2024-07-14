result = []
dump = []
def make_k_combinations(n, left, k):
    if k == 0:
        result.append(dump)
        for i in range(len(dump)):
            print(dump[i], end=' ')
        return 
    for i in range(left, n + 1):
        dump.append(i)
        # Recursive call:
        make_k_combinations(n, i + 1, k - 1)
        dump.pop()

def make_combinations(n, k):
    make_k_combinations(n, 0, k)
    return result

n = int(input())
k = int(input())
print(make_combinations(n, k))
