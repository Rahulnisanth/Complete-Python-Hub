import heapq

def format_output(N, result):
    print("[", end='')
    for i in range(N):
        print("[", end='')
        for j in range(2):
            if j != N - 1:
                print(f"{result[i][j]},", end='')
            else:
                print(f"{result[j][j]}", end='')
        if i != N - 1:
            print("],", end='')
        else:
            print("]", end='')
    print("]")


def getSkyline(buildings):
    N = len(buildings)
    points = []
    for left, right, height in buildings:
        points += [left, right]
    points = sorted(points)
    print(points)
    result = []
    i = 0
    max_heap = []
    for point in points:
        while i < N and buildings[i][0] <= point:
            left, right, height = buildings[i]
            heapq.heappush(max_heap, (-height, right))
            i += 1
        
        while max_heap and max_heap[0][1] <= point:
            heapq.heappop(max_heap)

        height = -max_heap[0][0] if max_heap else 0
        if not result or height != result[-1][1]:
            result += [(point, height)]
        
    return result


# Input drive :
buildings = [[0, 2, 3], [2, 5, 3]]
result = getSkyline(buildings)
format_output(len(result), result)
