# COMPUTE ALL THE POSSIBLE PERMUTATIONS OF AN ARRAY:
def  permutationsKUtil(nums) -> int:
      result = []

      def swap(arr, i, j):
          arr[i], arr[j] = arr[j], arr[i]

      def backtrack(res, arr, idx):
          if idx == len(arr):
              result.append(arr[:])
              return
          for i in range(idx, len(arr)):
              swap(arr, idx, i)
              backtrack(res, arr, idx + 1)
              swap(arr, idx, i)

      backtrack(result, nums, 0)
      return len(result)
