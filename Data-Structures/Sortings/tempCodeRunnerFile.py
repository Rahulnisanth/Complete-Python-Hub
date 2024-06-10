def selection_sort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)

# Input stream :
n = int(input())
data = list(map(int, input().split()))
selection_sort(data, n)