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


# DELETION IN BST :
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    # helper func
    def getLeftMax(node):
        maxx = node.val
        while node.right:
            maxx = node.right.val
            node = node.right
        return maxx

    if not root:
        return
    elif key < root.val:
        root.left = self.deleteNode(root.left, key)
    elif key > root.val:
        root.right = self.deleteNode(root.right, key)
    else:
        # case with no/one children:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # case with two children
        # get the max in left subtree
        else:
            root.val = getLeftMax(root.left)
            root.left = self.deleteNode(root.left, root.val)
    return root
