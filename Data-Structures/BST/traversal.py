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
    def in_order(self, node):
        if not node:
            return 
        self.in_order(node.left)
        print(node.data, end=' ')
        self.in_order(node.right)

    # pre-order:
    def pre_order(self, node):
        if not node:
            return 
        print(node.data, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    # post-order:
    def post_order(self, node):
        if not node:
            return 
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=' ')


# Main drive :
tree = BinarySearchTree()
n = int(input())
array = list(map(int, input().split()))
for key in array:
    tree.root = tree.insert(tree.root, key)
print("Inorder Traversal:", end=' ')
tree.in_order(tree.root)
print()
print("Preorder Traversal:", end=' ')
tree.pre_order(tree.root)
print()
print("Postorder Traversal:", end=' ')
tree.post_order(tree.root)
