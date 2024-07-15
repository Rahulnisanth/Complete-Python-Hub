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