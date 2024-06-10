def search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

# Input stream:
n = int(input())
data = list(map(int, input().split()))
k = int(input())
# Conditionals :
result =  search(data, k)
if result == 0: print(f"Element is present at location {result}\nBest Case")
if result == n - 1: print(f"Element is present at location {result}\nWorst Case")
if 0 < result < n - 1: print(f"Element is present at location {result}")
else: print("Element not found")