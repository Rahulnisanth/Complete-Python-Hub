def merge(arr, low, mid, high):
    temp = []
    left, right = low, mid + 1
    while left <= mid and right <= high :
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    # Remaining elements in left half :
    while left <= mid:
        temp.append(arr[left])
        left += 1
    # Remaining elements in right half :
    while right <= high:
        temp.append(arr[right])
        right += 1
    # Replacing the original - array :
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def divide(arr, low, high):
    # Recursively dividing and merging the array :
    if low == high: return 
    mid = (low + high) // 2
    divide(arr, low, mid)
    print(*arr)
    divide(arr, mid + 1, high)
    merge(arr, low, mid, high)


# Main drive function :
def merge_sort(arr, n):
    divide(arr, 0, n - 1)
    return arr

# Input stream :
nums = [45, 78, 12, 49, 11, 6]
merge_sort(nums, len(nums))