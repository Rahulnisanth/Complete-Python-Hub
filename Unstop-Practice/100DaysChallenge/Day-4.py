'''
Problem Statement
We are given a string s consisting of only lowercase letters of english, and a character ch.
Let the index of last occurrence of ch be idx, reverse the string from idx.
'''
def lastIndexOf(word, letter):
    for i in range(len(word)-1, -1, -1):
        if word[i] == letter: 
            return i
    return -1
def reverse(word):
    return word[::-1]

word = input().strip()
letter = str(input())
idx = lastIndexOf(word, letter)
print(word[:idx] + reverse(word[idx:]))


'''
Problem Statement
A machine could be fed with queries of type (a,b).
Where (a b) means we have a number ‘b’ ‘a’ times. 
Output the absolute difference between the number that appears most number of times and least number of times (least number of times must be at-least once. If there are multiple possible answers print the maximum possible absolute difference.
'''
n = int(input())
mapper = {}
for _ in range(n):
    count, num = list(map(int, input().split()))
    if num in mapper:
        mapper[num] += count
    else:
        mapper[num] = count

maxFreq = -1
minFreq = float('inf')
maxNum = None
minNum = None
for k, v in mapper.items():
    if v > maxFreq:
        maxFreq = v
        maxNum = k
    if v < minFreq:
        minFreq = v
        minNum = k

print(abs(maxNum - minNum))


'''
Problem Statement
Imagine you have a row of boxes. Each box can be either an "a" or a "b".
To check if it's an ab pattern, you need to make sure that all the "a" boxes, if they exist, come before any "b" boxes, if they exist.
If this order is maintained, it's an ab pattern; otherwise, it's not. Display "YES" if it is maintained else "NO". 
'''
pattern = str(input())
sorted_pattern = ''.join(sorted(pattern))
print("YES" if pattern == sorted_pattern else "NO")


'''
Problem Statement
Kritika has a collection of 2*n boxes, with n unique labels. Among them, one box is repeated n times.
How can Kritika identify and print the label of the repeated box?
'''
def findBox(mapper) -> int:
    for k, v in mapper.items():
        if v == n: 
            return k
    return -1
n = int(input())
n //= 2
nums = list(map(int, input().split()))
mapper = {}
for num in nums:
    if num in mapper: mapper[num] += 1
    else: mapper[num] = 1
print(findBox(mapper))
