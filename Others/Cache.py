def calculateOddSum(nums) -> int:
    left, right, total = 0, len(nums) - 1, 0
    while left <= right:
        if nums[left] % 2 != 0 :
            total += nums[left] 
        if nums[right] % 2 != 0:
            total += nums[right]
        left += 1
        right -= 1
    return total


# BITWISE MANIPULATION :
def tackle(n1, n2):
    if bin(n1)[-1] == '1' and bin(n2)[-1] == '1':
        n1 = n1 ^ n2
        n2 = n1 ^ n2
        n1 = n1 ^ n2
    if bin(n1)[-1] == '0' and bin(n2)[-1] == '0':
        n1 = n1 << 3
        n2 = n2 << 3
    return [n1, n2]
    
n1, n2 = list(map(int, input().split()))
print(tackle(n1, n2))

# IS SUM PRESENT IN ARRAY :
def is_found(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1):
            if i != j and nums[i] + nums[j] == k: return f"index1: {j}\nindex2: {i}"
    return "No two sum solution"

nums = list(map(int, input().split()))
k = int(input())
print(is_found(nums, k))


# ZIG-ZAG ROTATION OF STRINGS :
def reverse(word, start, end):
    while start < end:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1
def left_rotation(word, k):
    n = len(word)
    k %= n
    reverse(word, 0, n - 1)
    reverse(word, 0, n - k - 1)
    reverse(word, n - k, n - 1)
    return word
def right_rotation(word, k):
    n = len(word)
    k %= n
    reverse(word, 0, n - 1)
    reverse(word, 0, k - 1)
    reverse(word, k, n - 1)
    return word  
# Main stream of the program :
n = int(input())
for idx in range(n):
    input_string = [letter for letter in input()]
    k = int(input())
    if idx % 2 == 0: print("".join(left_rotation(input_string, k)))
    if idx % 2 != 0: print("".join(right_rotation(input_string, k)))


#  GUESSING GAME :
def guess_game(start, end, dp):
    if start < end:
        min_cost = float('inf')
        for guess in range(start, end + 1):
                cost = guess + max(guess_game(start, guess - 1, dp), guess_game(guess + 1, end, dp))
                min_cost = min(min_cost, cost)
        return min_cost
    else: return 0
# Input range:
n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
print(guess_game(1, n, dp))


# MAXIMUM SUM OF THE SUB-ARRAY :
def maxSum(array, n):
    dp = [float('-inf')] * (n + 1)
    dp[0], temp = array[0], 0
    for i in range(1, n + 1):
        temp = temp + array[i - 1]
        dp[i] = max(dp[i], temp)
    return dp[n]

arr = list(map(int, input().split()))
print(maxSum(arr, len(arr)))


# RECURRENCE SEQUENCE AFTER DECIMALS :
num, dnm = list(map(int, input().split()))
rem = num % dnm
map = {}
result = ''
while rem != 0 and rem not in map:
    map[rem] = len(result)
    rem *= 10
    result += str(rem // dnm)
    rem %= dnm
print(result[map[rem]:] if rem != 0 else '')

def checkSubarraySum(nums, k):
    if not nums: return False
    if k < 0: return False
    cummulative_sum = nums[0] + nums[1]
    for i in range(2, len(nums)):
        cummulative_sum += nums[i]
        if cummulative_sum % k == 0:
            return True
    return False
print(checkSubarraySum([23,2,6,4,7], 6))
print(checkSubarraySum([23,2,6,4,7], 13))