# DEPTH OF THE BINARY TREE :
def maxDepth(root) -> int:
    if root != None :
        left, right = maxDepth(root.left), maxDepth(root.right)
        return 1 + max(left, right)
    return 0


# IS SAME TREE :
def isSameTree(p, q):
    if p == None and q == None :
        return True
    if p != None and q != None and p.val == q.val :
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False


# INVERT THE BINARY TREE :
def invertTree(root):
    if not root: #Base Case
        return root
    invertTree(root.left) 
    invertTree(root.right)  

    root.left, root.right = root.right, root.left
    return root 


# CHECK THE BINARY TREE SYMMETRIC OR NOT :
def isSymmetric(root) -> bool:
    return DFS(root.left, root.right) if root != None else True
def DFS(leftNode, rightNode):
    if leftNode == None and rightNode == None:
        return True
    if leftNode == None or rightNode == None:
        return False
    
    return (leftNode.val == rightNode.val) and DFS(leftNode.left, rightNode.right) and DFS(leftNode.right, rightNode.left) 