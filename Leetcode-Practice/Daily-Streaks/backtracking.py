# COMBINATION SUM - II :
def combinationSum2(candidates, target):
    result = []
    candidates.sort()
    N = len(candidates)
    def backtrack(idx, dump, target):
        if target == 0:
            result.append(dump[:])
            return
        for i in range(idx, N):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            dump.append(candidates[i])
            backtrack(i + 1, dump, target - candidates[i])
            dump.pop()
    backtrack(0, [], target)
    return result


# COUNT THE SUB-ISLANDS IN THE GIVEN GRIDS:
def countSubIslands(grid1, grid2) -> int:
    def is_valid(x, y):
        return (0 <= x < len(grid1)) and (0 <= y < len(grid1[0]))
    
    def is_sub_island(x, y):
        if not is_valid(x, y) or grid2[x][y] != 1:
            return True
        if grid1[x][y] != 1:
            return False
        grid2[x][y] = 0
        result = True
        result &= is_sub_island(x + 1, y)
        result &= is_sub_island(x, y + 1)
        result &= is_sub_island(x - 1, y)
        result &= is_sub_island(x, y - 1)
        return result
        
    # core program :
    count = 0
    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            if grid2[i][j] == 1:
                if is_sub_island(i, j):
                    count += 1
    return count     


# MOST STONES REMOVED IN SAME ROW AND COL :
def removeStones(stones) -> int:
    def dfs(idx, visited, stones):
        visited[idx] = True
        for i in range(N):
            if not visited[i]:
                if stones[idx][0] == stones[i][0]:
                    dfs(i, visited, stones)
                if stones[idx][1] == stones[i][1]:
                    dfs(i, visited, stones)
    # main drive :
    N, count = len(stones), 0
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            count += 1
            dfs(i, visited, stones)
    return (N - count)


# DIFFERENT WAYS TO ADD PARENTHESIS :
def diffWaysToCompute(expression: str):
    def is_valid(op):
        return (op == '+' or op == '-' or op == '*')
    def backtrack(exp, memo):
        if exp in memo:
            return memo[exp]
        result = []
        for i in range(len(exp)):
            if is_valid(exp[i]):
                prefix = backtrack(exp[:i], memo)
                suffix = backtrack(exp[i + 1:], memo)
                for j in range(len(prefix)):
                    for k in range(len(suffix)):
                        if exp[i] == '+':
                            result.append(int(prefix[j]) + int(suffix[k]))
                        elif exp[i] == '-':
                            result.append(int(prefix[j]) - int(suffix[k]))
                        elif exp[i] == '*':
                            result.append(int(prefix[j]) * int(suffix[k]))
        # Edge case : 
        if len(result) == 0:
            result.append(int(exp))
        memo[exp] = result
        return result
    memo = {}
    return backtrack(expression, memo)


# TARGET SUM AFTER BUILDING EXPRESSION :
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    memo = {}
    def dfs(idx, curr_sum):
        if idx == len(nums):
            return 1 if curr_sum == target else 0
        if (idx, curr_sum) in memo:
            return memo[(idx, curr_sum)]
        add = dfs(idx + 1, curr_sum + nums[idx]) 
        sub = dfs(idx + 1, curr_sum - nums[idx])
        memo[(idx, curr_sum)] = add + sub
        return memo[(idx, curr_sum)]
    return dfs(0, 0)
