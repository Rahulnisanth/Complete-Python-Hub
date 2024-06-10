# SEARCHING IN BST :
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if val > root.val:
        return self.searchBST(root.right, val)
    if val < root.val:
        return self.searchBST(root.left, val)
    else:
        return root