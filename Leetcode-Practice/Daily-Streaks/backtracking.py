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