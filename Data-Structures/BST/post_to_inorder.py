class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def bst_constructor(self, array, start, end):
        if start > end:
            return None
        root = Node(array[end])
        idx = end - 1
        while idx >= start and array[idx] > root.data:
            idx -= 1
        root.left = self.bst_constructor(array, start, idx)
        root.right = self.bst_constructor(array, idx + 1, end - 1)
        return root

    def display(self, node):
        if not node:
            return
        self.display(node.left)
        print(node.data, end=' ')
        self.display(node.right)


# Input stream :
array = list(map(int, input().split()))
tree = BinaryTree()
tree.root = tree.bst_constructor(array, 0, len(array) - 1)
# print(*sorted(array))
tree.display(tree.root)