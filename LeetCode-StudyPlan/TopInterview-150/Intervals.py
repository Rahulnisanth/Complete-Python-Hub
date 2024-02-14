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