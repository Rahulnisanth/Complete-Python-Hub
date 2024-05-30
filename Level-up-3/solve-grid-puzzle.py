# DYNAMIC PROGRAMMING :
# CALCULATING THE NO. OF. POSSIBLE WAYS TO REACH THE END OF THE 2D GRID :
def solve_puzzle(row, col):
    dp = [[0] * (col + 1)] * (row + 1)
    dp[1][1] = 1
    for i in range(1, row + 1):
        for j in range(2, col + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[row][col]

row = int(input())
col = int(input())
print(solve_puzzle(row, col))


# IMPLEMENT THE CAN_SUM FUNCTION THATS TELLS WHETHER THE TARGET SUM IS FORMED USING THE ELEMENT OF NUMS
# THE ELEMENTS CAN BE USED ANY NUMBER OF TIMES :
def can_sum(target, nums):
    dp = [False] * (target + 1)
    dp[0] = True
    for i in range(target + 1):
        for j in range(len(nums)):
            if i + nums[j] <= target and dp[i]:
                dp[i + nums[j]] = True
    return "true" if dp[target] else "false"

target = int(input())
string = input().strip()
nums = list(map(int, string.replace("[","").replace("]","").replace(","," ").split()))
print(can_sum(target, nums))

