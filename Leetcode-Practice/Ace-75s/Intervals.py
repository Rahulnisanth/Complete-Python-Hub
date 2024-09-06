# MINIMUM NO. OF ARROWS TO BURST BALLOONS :
def findMinArrowShots(points) -> int:        
    # Sort the balloons based on their end coordinates
    points.sort(key=lambda x: x[1])
    arrows = 1
    prevEnd = points[0][1]
    # Count the number of non-overlapping intervals
    for i in range(1, len(points)):
        if points[i][0] > prevEnd:
            arrows += 1
            prevEnd = points[i][1]
    
    return arrows


# NON-OVERLAPPING INTERVALS :
def eraseOverlapIntervals(intervals) -> int:
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return count