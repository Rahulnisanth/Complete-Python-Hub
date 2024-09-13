def minBitFlips(start: int, goal: int) -> int:
    count = 0
    while start > 0 or goal > 0:
        if (start & 1) != (goal & 1):
            count += 1
        start >>= 1
        goal >>= 1
    return count


# XOR QUERIES OF THE SUB-ARRAY :
def xorQueries(arr, queries):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] ^ arr[i]
    result = []
    for left, right in queries:
        result.append(prefix[left] ^ prefix[right + 1])
    return result