# CONVERT THE SORTED ARRAY TO BINARY SEARCH TREE :
def sortedArrayToBST(nums):
    # Array > Tree conversion :
    def createTreeNode(nums, l, r):
        if l > r:
            return None
        else:
            mid = l + (r - l) // 2
            root = TreeNode(nums[mid])
            root.left = createTreeNode(nums, l, mid - 1)
            root.right = createTreeNode(nums, mid + 1, r)
            return root
    return createTreeNode(nums, 0, len(nums) - 1)
    
    