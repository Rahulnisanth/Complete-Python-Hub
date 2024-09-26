# BFS :
# Space Complexity: Proportional to the maximum width of the tree.
# 27 for the specific tree.
from collections import deque
def bfs(root):
    if not root:
        return
    queue = deque([root])
    result =[]
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.middle:
            queue.append(current.middle)
        if current.right:
            queue.append(current.right)


# DFS :
# Space Complexity: Proportional to the maximum depth of the tree.
# 4 for this specific tree.
def dfs(root):
    if not root:
        return
    result = []
    result.append(root.value)
    result.extend(dfs(root.left))
    result.extend(dfs(root.middle))
    result.extend(dfs(root.right))
    return result

