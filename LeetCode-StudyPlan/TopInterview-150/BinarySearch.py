# MEDIAN OF TWO SORTED ARRAYS :
def findMedianSortedArrays(nums1, nums2) -> float:
    nums1 += nums2
    nums1.sort()
    mid = len(nums1) // 2
    if len(nums1) % 2 == 0:
        return (nums1[mid] + nums1[(mid) - 1]) / 2
    else:
        return nums1[mid] 


# SEARCH INSERT POSITION :
def searchInsert(nums, target: int) -> int:
    start, mid = 0, 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return start
