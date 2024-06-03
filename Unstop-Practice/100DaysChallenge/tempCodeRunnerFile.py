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