def equalSubstring(s,t,maxCost) -> int:
    def helper(s1, s2):
        return abs(ord(s1) - ord(s2))
    idx, equalCount = 0, 0
    while idx < len(s) and maxCost > 0:
        print(f"{s[idx]} \t {t[idx]} \t {idx}")
        if s[idx] != t[idx]:
            cost = helper(s[idx], t[idx])
            if cost <= maxCost:
                maxCost -= cost
                print(f"{maxCost} -= {cost}")
                equalCount += 1
        elif s[idx] == t[idx]:
            equalCount += 1
        idx += 1
    return equalCount


print(equalSubstring("abcd","bcdf",3))
print(equalSubstring("abcd","cdef",3))
print(equalSubstring("abcd","acde",0))