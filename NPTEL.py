# NPTEL PROGRAMS:

def delchar(buffer, t):
    new_string = ""
    for i in buffer:
        if i == t:
            continue
        else:
            new_string += i
    print(new_string)


def primeproduct(n):
    prime_list = []
    for i in range(2, n):
        if n % i == 0:
            prime_list.append(i)
    isPrime = 0
    for j in range(len(prime_list) - 1):
        if (prime_list[j] * prime_list[j+1]) == n:
            isPrime = 1
        else:
            isPrime = 0
    if (isPrime):
        print(True)
    else:
        print(False)


def shuffle(l1, l2):
    min_len = min(len(l1), len(l2))
    shuffled = [item for pair in zip(
        l1[:min_len], l2[:min_len]) for item in pair]
    if len(l1) > min_len:
        shuffled.extend(l1[min_len:])
    elif len(l2) > min_len:
        shuffled.extend(l2[min_len:])
    return shuffled


def sum(li):
    sum = 0
    for i in li:
        sum += int(i)
    return sum


def sumsquare(l):
    new_list = []
    odd = []
    even = []
    for i in l:
        if i % 2 != 0:
            odd.append(i*i)
        else:
            even.append(i*i)
    new_list.extend([sum(odd), sum(even)])  # type: ignore
    print(new_list)


def expanding(l):
    new_list = []
    for i in range(len(l) - 1):  # type: ignore
        if l[i] > l[i+1]:
            new_list.append((l[i] - l[i+1]))
        else:
            new_list.append((l[i+1] - l[i]))
    count = 0
    for i in new_list:
        if new_list.count(i) == 1:
            count += 1
    if count == (len(new_list)):  # type: ignore
        sort_list = new_list[:]
        sort_list.sort()
        if (sort_list == new_list):
            return (True)
        else:
            return (False)
    else:
        return (False)


def transpose(matrix):
    row = len(matrix)  # type: ignore
    col = len(matrix[0])  # type: ignore
    transposed = []
    for j in range(col):
        transposed_row = []
        for i in range(row):
            transposed_row.append(matrix[i][j])
        transposed.append(transposed_row)
    return transposed  # type: ignore


# BINARY SEARCH ALGORITHM ~ T(N) = O(LOG N)
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



# INSERTION SORTING ~ T[N] = O(2N)
def insert_sort(l):
    for start in range(len(l)):
        pos = start
        while pos > 0 and l[pos] < l[pos - 1]:
            l[pos], l[pos - 1] = l[pos - 1], l[pos]
            pos -= 1
    return (l)



def histogram(l):
    counts = {}
    for num in l:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    print(counts)

    pairs = [(num, counts[num]) for num in sorted(counts.keys())]
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    return pairs



def transcript(coursedetails, studentdetails, grades):
    course_dict = dict(coursedetails)
    student_dict = dict(studentdetails)

    # Create a dictionary to store grades for each student
    student_grades = {}
    for roll, course, grade in grades:
        if roll not in student_grades:
            student_grades[roll] = []
        student_grades[roll].append((course, course_dict[course], grade))

    # Create the final transcript list
    transcript_list = []
    for roll, name in sorted(studentdetails, key=lambda x: x[0]):
        if roll in student_grades:
            sorted_grades = sorted(student_grades[roll], key=lambda x: x[0])
            transcript_list.append((roll, name, sorted_grades))

    return transcript_list


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



