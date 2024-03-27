# SUMMARY RANGES :
def summaryRanges(nums):
        if len(nums) < 1:
            return []
        else:
            lister = []
            start = nums[0]
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1] + 1:
                    if start == nums[i - 1]:
                        lister.append(str(start))
                    else:
                        lister.append(str(start) + "->" + str(nums[i - 1]))
                    start = nums[i]
            if start == nums[-1]:
                lister.append(str(start))
            else:
                lister.append(str(start) + "->" + str(nums[-1]))
    
            return lister


# MERGE INTERVALS :
def merge(intervals):
    if not intervals:
        return []
    else:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_merged_start, last_merged_end = merged[-1]
            
            if current_start <= last_merged_end:
                merged[-1] = [last_merged_start, max(last_merged_end, current_end)]
            else:
                merged.append([current_start, current_end])

        return merged


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