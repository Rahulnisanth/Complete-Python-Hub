def can_reach(hops, idx, dp) -> bool:
    # Base case
    if idx == n - 1: return True
    # Edge case
    if idx >= n or idx < 0 or dp[idx]: return False
    # Mark as dp :
    dp[idx] = True
    # Recursive approach
    return can_reach(hops, idx + hops[idx], dp)

# Input stream :
n = int(input())
hops = list(map(int, input().split()))
dp = [False] * (n)
print(can_reach(hops, 0, dp))