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


def solvePuzzle(n):
    def helper(dp, left, right):
        if left >= right:
            return 0
        if dp[left][right] != 0:
            return dp[left][right]
        else:
            result = float('inf') # max value:
            for guess in range(left, right + 1):
                temp = guess + max(helper(dp, guess + 1, right), helper(dp, left, guess - 1))
                result = min(result, temp)
        return result

    dp = [[0] * (n+1)] * (n+1)
    print(dp)
    helper(dp, 0, len(dp))

print(solvePuzzle(10))


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


# FINDING THE COMMON CHARACTERS :
def check_letter_presence(letter, words):
    for word in words:
        if letter not in word:
            return False
    return True

words = input().split()
result = ''
for letter in words[0]:
    if check_letter_presence(letter, words):
        result += letter
print(result)


