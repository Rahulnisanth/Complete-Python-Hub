def bubble_sort(nums, n):
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(*nums)

# Input Stream
n = int(input())
array = list(map(int, input().split()))
bubble_sort(array, n)