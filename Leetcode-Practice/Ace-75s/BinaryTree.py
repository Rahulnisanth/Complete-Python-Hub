# DEPTH OF THE BINARY TREE :
def maxDepth(root) -> int:
    if root != None :
        left, right = maxDepth(root.left), maxDepth(root.right)
        return 1 + max(left, right)
    return 0


# LEAF SIMILAR TREES :
def leafSimilar(root1, root2) -> bool:
    def helper(root, arr):
        if not root:
            return 
        if root.left == None and root.right == None:
            arr.append(root.val)
        helper(root.left, arr)
        helper(root.right, arr)
        return arr
    arr1 = helper(root1, [])
    arr2 = helper(root2, [])
    return arr1 == arr2


# COUNT GOOD NODES IN BINARY TREE :
def goodNodes(root) -> int:
    def dfs(node, maxVal):
        if not node: 
            return 0
        result = 1 if (node.val >= maxVal) else 0
        maxVal = max(maxVal, node.val)
        result += dfs(node.left, maxVal)
        result += dfs(node.right, maxVal)
        return result 
    return dfs(root, root.val)


# FIND THE LOWEST COMMON ANCESTOR :
def lowestCommonAncestor(root, p, q):
    if root in (None, p, q): 
        return root
    subs = [self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right)]
    return root if all(subs) else max(subs)


# RIGHT SIDE VIEW OF THE BINARY TREE :
from collections import deque
def rightSideView(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        lvl_size = len(q)
        for i in range(lvl_size):
            node = q.popleft()
            if i == lvl_size - 1:
                result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result


# MAXIMUM LEVEL SUM OF THE BINARY TREE :
def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    level = max_level = 1
    max_sum = float("-inf")
    q = [root]
    while q:
        level_sum = 0
        next_level = []
        for node in q:
            level_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
        q = next_level
        level += 1
    return max_level


# PATH SUM - III :
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    sums = defaultdict(int)
    sums[0] = 1

    def dfs(node, currSum):
        count = 0
        if node:
            currSum += node.val
            count += sums[currSum - targetSum]
            sums[currSum] += 1
            count += dfs(node.left, currSum) + dfs(node.right, currSum)
            sums[currSum] -= 1
        return count

    return dfs(root, 0)


# LONGEST ZIG-ZAG PATH IN BST :
def longestZigZag(self, root: Optional[TreeNode]) -> int:
    self.maxLength = 0

    def helper(node, length, direction):
        self.maxLength = max(self.maxLength, length)
        if node.left:
            (
                helper(node.left, length + 1, "left")
                if direction != "left"
                else helper(node.left, 1, "left")
            )
        if node.right:
            (
                helper(node.right, length + 1, "right")
                if direction != "right"
                else helper(node.right, 1, "right")
            )

    helper(root, 0, "")
    return self.maxLength
