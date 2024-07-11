class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.data:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        return node
    
    def is_valid(self, node):
        if not node: return True
        if node.left and node.left.data > node.data: return False
        if node.right and node.right.data < node.data: return False
        return self.is_valid(node.left) and self.is_valid(node.right)

# Main drive :
tree = BinarySearchTree()
for _ in range(7):
    tree.root = tree.insert(tree.root, int(input()))
# Printing :
print(tree.is_valid(tree.root))