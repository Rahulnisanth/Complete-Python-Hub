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


# PATH SUM OF BINARY TREE :
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    leftSum = hasPathSum(root.left, targetSum - root.val)
    rightSum = hasPathSum(root.right, targetSum - root.val)
    return leftSum or rightSum


# COUNT THE TREE NODES :
def countNodes(root) -> int:
    if root == None:
        return 0
    elif root.right == None:
        return countNodes(root.left) + 1
    elif root.left == None:
        return countNodes(root.right) + 1

    return countNodes(root.left) + countNodes(root.right) + 1


# AVERAGE LEVELS OF THE BINARY TREE :
from collections import deque
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []
    else:
        result = []
        queue = deque([root])
        
        while queue:
            levelSize = len(queue)
            levelSum = 0

            for _ in range(levelSize):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(levelSum / levelSize)

        return result


# SUM ROOT TO LEAF NUMBERS ;
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(node, placer):
        if not node:
            return 0
        placer = placer * 10 + node.val
        if not node.left and not node.right:
            return placer
        else:
            return dfs(node.left, placer) + dfs(node.right, placer)
    return dfs(root, 0)

