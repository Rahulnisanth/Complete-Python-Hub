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


# FINDING THE PEAK ELEMENT :
def findPeakElement(nums) -> int:
    start, end = 0, len(nums) - 1
    mid = 0

    while start < end:
        mid = (start + end) // 2
        if nums[mid] > nums[mid + 1]:
            end = mid
        else:
            start = mid + 1
    
    return start


# SEARCH IN A 2D ARRAY / MATRIX :
def searchMatrix(matrix, target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    start, end = 0, (rows * cols) - 1

    while start <= end:
        mid = (start + end) // 2
        midVal = matrix[mid // cols][mid % cols]
        if midVal == target:
            return True
        elif midVal < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return False


# SEARCH TARGET IN ROTATED ARRAY :
def search(nums, target: int) -> int:
    if not nums:
        return -1
    else:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


# FIND THE FIRST & LAST INDEX OF THE TARGET :
def searchRange(nums, target: int):
    def binaryLeft(nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
    
    def binaryRight(nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return end
    
    leftIndex = binaryLeft(nums, target)
    rightIndex = binaryRight(nums, target)

    if leftIndex <= rightIndex:
        return [leftIndex, rightIndex]
    else:
        return [-1, -1]


# SEARCH MINIMUM ELEMENT IN A ROTATED SORTED ARRAY :
def findMin(nums) -> int:
    start, end = 0, len(nums) - 1
    if nums[start] < nums[end]:
        return nums[start]
    else:
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
                
        return nums[start]