# SORT THE NUMBERS IN LEXICOGRAPHICAL ORDER :
def lexicalOrder(n: int):
    result = []
    def dfs(current):
        if current > n:
            return 
        result.append(current)
        for i in range(10):
            next_num = current * 10 + i
            if next_num > n:
                break
            dfs(next_num)
    for i in range(1, 10):
        if i <= n:
            dfs(i)
    return result
    # OR
    # result = sorted([i for i in range(1, n + 1)], key=str)
    # return result