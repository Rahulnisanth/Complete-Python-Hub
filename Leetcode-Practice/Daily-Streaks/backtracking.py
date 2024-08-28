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