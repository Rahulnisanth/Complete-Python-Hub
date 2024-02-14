# MEDIAN OF TWO SORTED ARRAYS :
def findMedianSortedArrays(nums1, nums2) -> float:
    nums1 += nums2
    nums1.sort()
    mid = len(nums1) // 2
    if len(nums1) % 2 == 0:
        return (nums1[mid] + nums1[(mid) - 1]) / 2
    else:
        return nums1[mid] 
