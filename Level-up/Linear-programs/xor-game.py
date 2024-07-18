# MAXIMUM [X] IN THE XOR-GAME :
def xor_game(K, arr):
    dump = 0
    for num in arr:
        dump += (num ^ K)
    return dump

def start_game(x, arr):
    arrSum = sum(arr)
    for i in range(x + 1):
        xorSum = xor_game(i, arr)
        if xorSum > arrSum:
            arrSum = xorSum
    return arrSum

# Input drive :
n = int(input())
x = int(input())
arr = [int(input()) for _ in range(n)]
print(start_game(x, arr))