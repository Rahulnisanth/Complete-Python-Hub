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
    
    # in-order:
    def display(self, node):
        if not node:
            return 
        self.display(node.left)
        print(node.data, end=' ')
        self.display(node.right)



# Main drive :
tree = BinarySearchTree()
n = int(input())
array = list(map(int, input().split()))
for key in array:
    tree.root = tree.insert(tree.root, key)
# Printing :
tree.display(tree.root)