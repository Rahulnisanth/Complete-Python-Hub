def target_sum_combinations(test_cases):
    results = []
    for case in test_cases:
        n, array, target = case
        array.sort()
        combinations = []
        def backtrack(start, path, target):
            if target == 0:
                combinations.append(path[:])
                return
            for i in range(start, n):
                if i > start and array[i] == array[i - 1]:
                    continue
                if array[i] > target:
                    break
                path.append(array[i])
                backtrack(i + 1, path, target - array[i])
                path.pop()
        backtrack(0, [], target)
        if not combinations:
            results.append("Empty")
        else:
            dumps = ''.join(['( ' + ' '.join(map(str, dump)) + ' )' for dump in combinations])
            results.append(dumps)
    return results

# Input Stream :
_test = int(input().strip())
test_cases = []
for _ in range(_test):
    N = int(input().strip())
    array = list(map(int, input().strip().split()))
    B = int(input().strip())
    test_cases.append((N, array, B))

results = target_sum_combinations(test_cases)
for result in results:
    print(result)
