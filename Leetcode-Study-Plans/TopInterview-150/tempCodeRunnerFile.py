def resetKthBit(N, K):
    # Create a mask with all bits set to 1 except for the K-th bit
    mask = ~(1 << (K - 1))
    print
    # Use bitwise AND to reset the K-th bit of N
    result = N & mask
    
    return result

# Example usage:
N = 5
K = 1
print(resetKthBit(N, K))