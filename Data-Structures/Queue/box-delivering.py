def solveBoxGame(N, boxes, maxBoxes, maxWeight):
    def backtrack(idx):
        # Base case:
        if idx >= N: 
            return 0
        # Main play :
        j = k = idx
        w = b = extra = 0
        while j < N and b < maxBoxes and w + boxes[j][1] <= maxWeight:
            b += 1
            w += boxes[j][1]
            if j != idx and boxes[j][0] != boxes[j - 1][0]:
                extra += 1
                k = j
            j += 1
        # Other handlings :
        trip = 2 + extra + backtrack(j)
        if k != idx:
            trip = min(trip, 1 + extra + backtrack(k))
        return trip
    # Invoke tracking :
    return backtrack(0)

# Input stream :
N = int(input())
buffer = input().replace('[','').replace(']','').split(',')
boxes = [[int(buffer[i]), int(buffer[i + 1])] for i in range(0, len(buffer), 2)]
print(boxes)
portsCount = int(input())
maxBoxes = int(input())
maxWeight = int(input())
print(f"Result: {solveBoxGame(N, boxes, maxBoxes, maxWeight)}")