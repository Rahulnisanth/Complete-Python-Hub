# DELETION IN BST:
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.data:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        return node
    
    def delete(self, node, delKey):
        if not node:
            return node
        if delKey < node.data:
            node.left = self.delete(node.left, delKey)
        if delKey > node.data:
            node.right = self.delete(node.right, delKey)
        else:
            # Case for 0 or 1 child :
            if not node.left: return node.right
            if not node.right: return node.left
            # Case for 2 child :
            else:
                # Way - 1 [Can replace the node value with the right minimum]
                node.data = self.helper_1(node.right)
                node.right = self.delete(node.right, node.data)
                # Way - 2 [Can replace the node value with left maximum]
                # node.data = self.helper_2(node.left)
                # node.left = self.delete(node.left, node.data)
        return node

    # Helper for finding the minimum node in right sub-tree :
    def helper_1(self, node) -> int:
        minx = node.data
        while node.left:
            minx = node.data
            node = node.left
        return minx
    
    # Helper for finding the maximum node in left sub-tree :
    def helper_2(self, node) -> int:
        maxx = node.data
        while node.right:
            maxx = node.data
            node = node.right
        return maxx

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
K = int(input())
for key in array:
    tree.root = tree.insert(tree.root, key)
tree.root = tree.delete(tree.root, K)
# Printing :
tree.display(tree.root)
