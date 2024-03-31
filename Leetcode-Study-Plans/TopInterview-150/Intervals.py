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
