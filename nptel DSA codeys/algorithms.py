# PYTHON ALGORITHMS :-

# QUICK SORTING ALGORITHM ~ T[N] = O(N^2)
def quick_sort(A, l, r):
    # Base case for no elements or 1 element in list :
    if r - l <= 1:
        return ()
    # LET l => pivot,
    # yellow => small elements,
    # green => large elements
    yellow = l + 1
    for green in range(l+1, r):
        if A[green] <= A[l]:
            (A[yellow], A[green]) = (A[green], A[yellow])
            yellow += 1
    # Swapping the pivot and the yellow element...
    A[l], A[yellow - 1] = A[yellow - 1], A[l]
    # Recursive call...
    quick_sort(A, l, yellow - 1)
    quick_sort(A, yellow, r)
    return (A)


# MERGE SORTING ALGORITHM :
def merge(a, b):
    (c, m, n) = ([], len(a), len(b))
    (i, j) = (0, 0)
    while i+j < m+n:
        # Case if A is empty or head of list[a] is greater...
        if i == m or a[i] > b[j]:
            c.append(b[j])
            j = j+1
        # Case if B is empty or head of the list[a] is smallest...
        elif j == n or a[i] <= b[j]:
            c.append(a[i])
            i = i+1
    return (c)


def merge_sort(a, left, right):
    # Case for list with 1 or no elements...
    if right - left <= 1:
        return a[left:right]
    # Case for list with more than 1 elements...
    if right - left > 1:
        mid = (left+right)//2
        l = merge_sort(a, left, mid)  # parsing the left half of the list
        r = merge_sort(a, mid, right)  # parsing the right half of the list
        return (merge(l, r))  # Merging the left and right halves after parsing


# INSERTION SORTING ~ T[N] = O(2N)
def insert_sort(l):
    for start in range(len(l)):
        pos = start
        while pos > 0 and l[pos] < l[pos - 1]:
            l[pos], l[pos - 1] = l[pos - 1], l[pos]
            pos -= 1
    return (l)


# BINARY SEARCH ALGORITHM ~ T(N) = O(LOG N//2)
def bin_search(seq, v, l, r):
    if (r - l == 0):
        return False
    mid = (l + r) // 2  # Middle index of the sorted list
    if (v == seq[mid]):
        return True
    elif (v < seq[mid]):
        return bin_search(seq, v, l, mid)
    else:
        return bin_search(seq, v, mid+1, r)


# SELECTION SORTING ALGORITHM ~ T[N] = O(2N)
def select_sort(l):
    for start in range(len(l)):
        min_pos = start
        for i in range(start, len(l)):
            if l[i] < l[min_pos]:
                min_pos = i
        (l[start], l[min_pos]) = (l[min_pos], l[start])
    return (l)


# LINEAR SEARCH ALGORITHM ~ T(N) = O(LOG N)
def l_search(arr, v):
    for i in range(0, len(arr)):
        if arr[i] == v:
            return ('Found')
    return None

arr = [i for i in range(0, 100, 2)]
v = 88
print('Search status :', l_search(arr, v))