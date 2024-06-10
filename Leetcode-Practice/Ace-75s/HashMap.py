# FIND THE DIFFERENCE OF TWO ARRAYS :
def findDifference(nums1, nums2):
    first = list(set(nums1) - set(nums2))
    second = list(set(nums2) - set(nums1))
    return [first, second]