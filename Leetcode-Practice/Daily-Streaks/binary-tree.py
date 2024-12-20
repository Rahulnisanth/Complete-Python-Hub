# CREATION OF BINARY TREE FROM GIVEN DESCRIPTION :
'''
You are given a 2D integer array descriptions where descriptions[i] = [parent[i], child[i], isLeft[i]] indicates that parent[i] is the parent of child[i] in a binary tree of unique values. Furthermore,
If isLeft[i] == 1, then child[i] is the left child of parent[i].
If isLeft[i] == 0, then child[i] is the right child of parent[i].
Construct the binary tree described by descriptions and return its root.
The Test cases will be generated such that the binary tree is valid.
'''
def createBinaryTree(descriptions):
    nodes = {}
    children = set()
    for parent, child, isLeft in descriptions:
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)
        if isLeft == 1:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
        children.add(child)
    for parent, child, isLeft in descriptions:
        if parent not in children:
            return nodes[parent]


# STEP-BY-STEP DIRECTIONS FROM ONE NODE TO ANOTHER :
'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
'''
def getDirections(root, startValue: int, destValue: int) -> str:
    def find_path(node, key, path):
        if node.val == key:
            return True
        if node.left and find_path(node.left, key, path):
            path.append('L')
        elif node.right and find_path(node.right, key, path):
            path.append('R')
        return path
    # Main drive :
    start, dest = [], []
    find_path(root, startValue, start)
    find_path(root, destValue, dest)
    while len(start) and len(dest) and start[-1] == dest[-1]:
        start.pop()
        dest.pop()
    return ''.join("U" * len(start)) + "".join(dest[::-1])


# DELETE NODES AND RETURN THE FOREST :
'''
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.
'''
def delNodes(root, to_delete):
    to_delete = set(to_delete)
    result = []
    def helper(node, is_root):
        if not node: 
            return None
        is_deleted = node.val in to_delete
        if is_root and not is_deleted:
            result.append(node)
        node.left = helper(node.left, is_deleted)
        node.right = helper(node.right, is_deleted)
        return None if is_deleted else node
    helper(root, True)
    return result


# KTH LARGEST LEVEL SUM IN THE BINARY TREE :
import heapq
from collections import deque
def kthLargestLevelSum(root, k: int) -> int:
    if not root:
        return -1
    heap = []
    def level_traversal(node):
        if not node:
            return -1
        q = deque([node])
        while q:
            lvl_size = len(q)
            adder = 0
            for _ in range(lvl_size):
                current = q.popleft()
                adder += current.val
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            heapq.heappush(heap, adder)
            if len(heap) > k:
                heapq.heappop(heap)
    level_traversal(root)
    return heap[0] if len(heap) >= k else -1 


# HEIGHT OF THE BINARY TREE AFTER REMOVAL OF SUBTREE QUERIES :
def treeQueries(self, root, queries):
    # pre-calculate height for each node: left subtree height and right subtree height
    levels = {}
    heights = {}
    calculateHeightDepth(root, 0, heights, levels)

    for key, val in levels.items():
        levels[key] = sorted(levels[key], key=lambda x: x[1], reverse=True)
    
    answer = []
    for query in queries:
        ans = calculateQuery(query, heights, levels)
        answer.append(ans)
    return answer

def calculateHeightDepth(node, cur_height, heights, levels):
    if not node:
        return -1
    
    heights[node.val] = cur_height
    
    
    left = calculateHeightDepth(node.left, cur_height + 1, heights, levels)
    right = calculateHeightDepth(node.right, cur_height + 1, heights, levels)
    depth = 1 + max(left, right)
    if levels.get(cur_height):
        levels[cur_height].append((node.val, depth))
    else:
        levels[cur_height] = [(node.val, depth)]
    return depth

def calculateQuery(query, heights, levels):
    level = heights[query]
    same_level = levels[level]
    max_depth = 0
    for node, depth in same_level:
        if node != query:
            return  depth + level if len(same_level) > 1 else level - 1
    return level - 1

# REVERSE ODD LEVELS OF PERFECT BINARY TREE 
def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    self.traverse_dfs(root.left, root.right, 0)
    return root
def traverse_dfs(self, leftNode, rightNode, level):
    if not leftNode or not rightNode:
        return
    if level % 2 == 0:
        leftNode.val, rightNode.val = rightNode.val, leftNode.val
    self.traverse_dfs(leftNode.left, rightNode.right, level + 1)
    self.traverse_dfs(leftNode.right, rightNode.left, level + 1)
