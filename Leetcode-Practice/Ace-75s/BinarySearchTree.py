# SEARCHING IN BST :
def searchBST(root, val: int):
    if not root:
        return None
    if val > root.val:
        return self.searchBST(root.right, val)
    if val < root.val:
        return self.searchBST(root.left, val)
    else:
        return root