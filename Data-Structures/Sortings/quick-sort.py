def partition(arr, low, high):
    # Choosing the pivot as first element in un-sorted array ...
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        # Left sub-array ...
        while i < high and arr[i] <= pivot:
            i += 1
        # Right sub-array ...
        while j > low and arr[j] > pivot:
            j -= 1
        # If crossed the bound ...
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # Moving the pivot to correct position :
    arr[low], arr[j] = arr[j], arr[low]
    # Returning the pivot index ... 
    return j


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        print(array)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# Input stream :
size = int(input())
data = list(map(int, input().split()))
quickSort(data, 0, size - 1)
