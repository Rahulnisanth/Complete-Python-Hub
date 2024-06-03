'''
Problem Statement
Mocha is given yet another task. In the task, mocha is provided with a sequence of n numbers.
In the sequence for every number, we have to find the count of elements that are strictly smaller than it and generate a sequence from it.
Your task is to help mocha in building the sequence.
'''
def smallest_sequence_count(nums, n):
    counts = [0] * n
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] < nums[i]: count += 1
        counts[i] = count
    return counts

n = int(input())
nums = list(map(int, input().split()))
print(*smallest_sequence_count(nums, n))

