# MIN OPERATIONS TO EXCEED THE THRESHOLD VALUE II :
def minOperations(self, nums: List[int], k: int) -> int:
      count = 0
      heapify(nums)
      while len(nums) >= 2 and nums[0] < k:
          x = heappop(nums)
          y = heappop(nums)
          opt = (min(x, y) * 2) + max(x, y)
          heappush(nums, opt)
          count += 1
      return count
