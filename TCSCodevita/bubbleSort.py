def bubble_sort(arr):
    n = len(arr)

    def asCending(arr, n):
        swap = 0
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    swap += 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return swap

    def dsCending(arr, n):
        swap = 0
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] < arr[j + 1]:
                    swap += 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return swap

    asOrder = asCending(arr.copy(), n)
    dsOrder = dsCending(arr, n)

    return min(asOrder, dsOrder)




