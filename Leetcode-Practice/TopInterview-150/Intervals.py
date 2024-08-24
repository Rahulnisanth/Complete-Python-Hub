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
    intervals.sort(key=lambda x: x[0])
    stack = [intervals[0]]
    for i in range(1, len(intervals)):
        start, end = stack[-1]
        if intervals[i][0] <= end:
            stack[-1] = [start, max(end, intervals[i][1])]
        else:
            stack.append(intervals[i])
    return stack
    