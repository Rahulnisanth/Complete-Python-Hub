# CREATING VALID IP ADDRESS USING THE GIVEN STRING :
def restoreIpAddresses(buffer):
    result = []
    parts = []
    
    # Backtracking the valid ip addresses :
    def backtrack(buffer, parts, result):
        if not buffer and len(parts) == 4:
            buffer = '.'.join(parts[::-1])
            result.append(buffer)
            return
        for i in range(1, min(3, len(buffer)) + 1):
            if int(buffer[:i]) >= 0 and int(buffer[:i]) <= 255:
                if i > 1 and buffer[0]=='0': 
                    continue
                else:
                    backtrack(buffer[i:], [buffer[:i]] + parts, result)
        return
    
    # Main drive :
    backtrack(buffer, parts, result)
    return result

# Input drive :
buffer = input().strip()
print(restoreIpAddresses(buffer))
