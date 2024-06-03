def ThreeSumCloset(nums: [int], target: int) -> int:
      # Sort the input list for easier sum comparisons.
      nums.sort()
      
      # Initialize the 'result' variable to positive infinity and get the length of 'nums'.
      result, n = float('inf'), len(nums)
      
      # Iterate through 'nums' from the first element to the third-to-last element.
      for i in range(n-2):
      # Initialize two pointers 'left' and 'right' to find the triplet sum.
            left, right = i+1, n-1

      # Continue searching for the closest sum while 'left' and 'right' pointers haven't crossed.
            while left < right:
                  # Calculate the sum of the current triplet.
                  closet_sum = nums[i] + nums[left] + nums[right]
                  
                  # Update 'result' if the absolute difference between the current sum and the target
                  # is smaller than the absolute difference between the previous 'result' and the target.
                  if abs(closet_sum - target) < abs(result - target):
                        result = closet_sum
                        
                  # Adjust 'left' and 'right' pointers based on the comparison with the target.
                  if closet_sum < target:
                        left += 1
                  else:
                        right -= 1

      # Return the 'result,' which holds the closest sum to the 'target.'
      return result
