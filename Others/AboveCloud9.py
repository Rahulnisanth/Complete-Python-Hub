# BFS :
from collections import deque
def bfs(root):
    def bfs_helper(node):
        if not node:
            return 
        q = deque([node])
        while q:
            curr = q.popleft()
            print(curr.value) 
            if curr.left:
                q.append(curr.left)
            if curr.middle:
                q.append(curr.middle)
            if curr.right:
                q.append(curr.right)
    return bfs_helper(root)


# DFS :
def dfs(root):
    def dfs_helper(node):
        if not node:
            return 
        print(node.value)
        dfs_helper(node.left)
        dfs_helper(node.middle)
        dfs_helper(node.right)
    return dfs_helper(root)

