def binary_search(data, k):
    count = 0
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        count += 1
        if data[mid] == k: 
            return [mid, count]
        if data[mid] < k: 
            low = mid + 1
        else: 
            high = mid - 1
    return [-1, count]

# Input stream:
n = int(input())
data = list(map(int, input().split()))
k = int(input())
idx, count = binary_search(data, k)
if idx > 0: print(f"{k} found at location {idx}\n{count} comparisons are done")
if idx < 0: print(f"Not found\n{count} comparisons are done")
