# N P T E L  ASSIGNMENTS :-

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







