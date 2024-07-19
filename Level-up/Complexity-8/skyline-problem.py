from collections import defaultdict
import heapq


class BuildingPoint:
    def __init__(self, x, is_start, height):
        self.x = x
        self.is_start = is_start
        self.height = height
    
    def __lt__(self, other):
        # The same X for two start points...
        if self.x != other.x:
            return self.x < other.x
        # The same X for two end points...
        if self.is_start != other.is_start:
            return self.is_start > other.is_start
        # The same X for start & end >> Start has to be prioritized...
        else:
            return self.height > other.height if self.is_start else self.height < other.height


def format_output(N, result):
    print("[", end='')
    for i in range(N):
        print("[", end='')
        for j in range(2):
            if j != N - 1:
                print(f"{result[i][j]},", end='')
            else:
                print(f"{result[i][j]}", end='')
        if i != N - 1:
            print("],", end='')
        else:
            print("]", end='')
    print("]")


def getSkyline(buildings):
    buildingPoints = []
    for building in buildings:
        buildingPoints.append(BuildingPoint(building[0], True, building[2]))
        buildingPoints.append(BuildingPoint(building[1], False, building[2]))
    buildingPoints.sort()
    result = []
    height_map = defaultdict(int)
    height_map[0] = 1
    prev_max_height = 0
    max_heap = [0]

    for build_point in buildingPoints:
        if build_point.is_start:
            height_map[build_point.height] += 1
            heapq.heappush(max_heap, -build_point.height)
        else:
            height_map[build_point.height] -= 1

        while max_heap and height_map[-max_heap[0]] == 0:
            heapq.heappop(max_heap)

        current_max = -max_heap[0] if max_heap else 0
        if prev_max_height != current_max:
            result.append([build_point.x, current_max])
            prev_max_height = current_max
        
    return result


# Input drive :
buildings = eval(input())
result = getSkyline(buildings)
format_output(len(result), result)
