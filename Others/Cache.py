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


def check_sub_array_sum(nums, k):
    if not nums: return False
    if k < 0: return False
    prefix_sum = nums[0] + nums[1]
    for i in range(2, len(nums)):
        prefix_sum += nums[i]
        if prefix_sum % k == 0:
            return True
    return False
print(check_sub_array_sum([23,2,6,4,7], 6))
print(check_sub_array_sum([23,2,6,4,7], 13))


def sortColors(nums):
    '''
    Do not return anything modify the original array
    '''
    red = nums.count(0) 
    white = nums.count(1)
    blue = nums.count(2)
    nums[:red] = [0] * red
    nums[red:red+white] = [1] * white
    nums[white:white+blue] = [2] * blue

nums = [2,0,1]
sortColors(nums)
print(nums)


# Python3 implementation of the approach 
def valid(cnt): 
	for i in range(0, 26): 
		if cnt[i] >= 2: 
			return False
	return True


def getGoodString(s, n): 
	if n < 26:
		return "-1"
	for i in range(25, n): 
		cnt = [0] * 26
		for j in range(i, i - 26, -1): 
			if s[j] != '?':
				cnt[ord(s[j]) - ord('a')] += 1
		if valid(cnt): 
			cur = 0
			while cur < 26 and cnt[cur] > 0: 
				cur += 1
			for j in range(i - 25, i + 1): 
				if s[j] == '?':
					s[j] = chr(cur + ord('a')) 
					cur += 1
					while cur < 26 and cnt[cur] > 0:
						cur += 1
			return ''.join(s) 
	return "-1"

# Input stream :
buffer = input()
print(getGoodString(buffer))


def validate_passkey(buffer) -> str:
    if len(buffer) < 8:
        return "Your Password is Not Strong"
    spl_count = num_count = upper_count = lower_count = 0
    for ch in buffer:
        if ch.isdigit(): num_count += 1
        if ch.isalpha() and ch.islower(): lower_count += 1
        if ch.isalpha() and ch.isupper(): upper_count += 1
        else: spl_count += 1
    return "Your Password is Strong" if spl_count >= 1 and\
                                        num_count >= 1 and\
                                        upper_count >= 1 and\
                                        lower_count >= 1 \
        else "Your Password is Not Strong"

# Input :
buffer = input()
print(validate_passkey(buffer))



def countIslands(grid):
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def mark_islands(i, j):
        if is_valid(i, j) and grid[i][j] == "1":
            grid[i][j] = "0"
            mark_islands(i + 1, j)
            mark_islands(i - 1, j)
            mark_islands(i, j + 1)
            mark_islands(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                mark_islands(i, j)
    return count


# Input drive :
grid = eval(input())
print(countIslands(grid))




def longest_consecutive_sequence(nums):
    nums = set(nums)
    ans = 0
    mapper = {}

    for num in nums:
        if num - 1 not in nums:
            temp = num
            current_length = 1
            while temp + 1 in nums:
                temp += 1
                current_length += 1
            if current_length in mapper:
                mapper[current_length] += 1
            else:
                mapper[current_length] = 1
            ans = max(ans, current_length)

    if ans in mapper and mapper[ans] > 1:
        return 0
    else:
        return ans

# Sample inputs
array = list(map(int, input().split()))
print(longest_consecutive_sequence(array))


