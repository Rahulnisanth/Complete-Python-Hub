def insertion_sort(nums, n):
    for i in range(n):
        k = i
        while k > 0 and nums[k] < nums[k - 1]:
            nums[k], nums[k - 1] = nums[k - 1], nums[k]
            k -= 1
        print(*nums)

# Input stream :
n = int(input())
nums = list(map(int, input().split()))
insertion_sort(nums, n)