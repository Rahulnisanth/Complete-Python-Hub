# SEARCH IN ROTATED SORTED ARRAY II :
def search(self, nums: List[int], target: int) -> bool:
      left, right = 0, len(nums) - 1
      while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
              return True
          while left < mid and nums[left] == nums[mid]:
              left += 1
          while right < mid and nums[right] == nums[mid]:
              right -= 1
          if nums[left] <= nums[mid]:
              if nums[left] <= target < nums[mid]:
                  right = mid - 1
              else:
                  left = mid + 1  
          else:
              if nums[mid] < target <= nums[right]:
                  left = mid + 1
              else:
                  right = mid - 1
      return False
