'''
Problem Statement
Ravi discovered that some strings read the same forwards and backwards, which are called palindromes.
He noticed that every string he encountered has at least one palindromic substring. He wants to know how to find the longest palindromic substring in a given string.
Can you help him determine the length of this longest palindromic substring?
'''
def longest_palindromic_substring(word) -> int:
    n = len(word)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # Marking true for single characters :
    maxLength = 1
    i = 0
    while i < n:
        dp[i][i] = True
        i += 1
    # Marking true if double characters appears :
    start = 0
    i = 0
    while i < n - 1:
        if word[i] == word[i + 1]:
            dp[i][i + 1] = True
            start = i
            maxLength = 2
        i += 1
    # Checking for palindrome more than 2 :
    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and word[i] == word[j]:
                dp[i][j] = True
                if k > maxLength:
                    start = i
                    maxLength = k
            i += 1
        k += 1
    return maxLength

word = input()
print(longest_palindromic_substring(word))


'''
Problem Statement
Each Christmas, the members of the royal family exchange gifts with each other. The family has n members numbered from 1 to n. However, not everyone in the family gives and receives the same number of gifts.
The youngest member receives a gift from everyone else in the family except himself but does not give any gifts to anyone else. This Christmas, there were a total of m gifts that were exchanged among the family members. You are provided with the data for all m gifts.
Find the number that represents the youngest family member using the given data.
'''
def find_youngest(n, m, gifts) -> int:
    sent_count = [0] * (n + 1)
    received_count = [0] * (n + 1)
    for gift in gifts:
        sender, receiver = gift
        sent_count[sender] += 1
        received_count[receiver] += 1
    for member in range(1, n + 1):
        if received_count[member] == n - 1 and sent_count[member] == 0:
            return member
    return -1

n, m = list(map(int, input().split()))
gifts = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    gifts.append((a, b))

print(find_youngest(n, m, gifts))


'''
Problem Statement
Given an integer array, arr. Display the count of AND triplets.
An AND triplet is a set of three indices i, j, and k such that:
0 <= i<arr.length
0 <= j <arr.length
0 <= k <arr.length
arr[i] &arr[j] &arr[k] == 0, where & represents the bitwise-AND operator.
'''
def find_triplets(arr, n) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result = arr[i] & arr[j] & arr[k]
                if result == 0: count += 1
    return count

n = int(input())
array = list(map(int, input().split()))
print(find_triplets(array, n))


'''
Problem Statement
In a peculiar basketball game, where World Cup is happening, Aniket is tasked with keeping the scores of the match. The game unfolds in rounds, and with each rounds there is a syste like thematches played previously will be highlighted in future scores too i.e where the scores of previous rounds can influence those in the future.
He is provided with a list of operations, represented by strings, denoted as 'ops'.
Each operation, 'ops[i]', can be one of the following: an integer 'x', indicating the recording of a new score 'x'; a '+', which means recording a score that is the sum of the previous two scores (and it is ensured that there are always two previous scores available); 'D', signifying recording a score that is double the previous score (and there is always a previous score); or 'C', indicating the invalidation of the previous score, removing it from the record (and it is ensured that there is always a previous score to remove).
Aniket's task is to process these operations and calculate the sum of all the scores and keep record of it for the final judgement.
'''
def result(ops):
    stack = []
    for op in ops:
        if op == 'C': 
            if stack: stack.pop()
        elif op == 'D': 
            if stack: stack.append(stack[-1] * 2)
        elif op == '+': 
            if len(stack) >= 2: stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)

n = int(input())
ops = input().split()
print(result(ops))