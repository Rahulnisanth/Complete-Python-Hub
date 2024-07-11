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
    
    
    def find_common_ancestor(self, node, n1, n2):
        if not node:
            return None
        if node.data > n1 and node.data > n2:
            return self.find_common_ancestor(node.left, n1, n2)
        if node.data < n1 and node.data < n2:
            return self.find_common_ancestor(node.right, n1, n2)
        return node


    def measure_distance(self, node, key):
        if not node:
            return -1
        if node.data == key:
            return 0
        if key < node.data:
            return 1 + self.measure_distance(node.left, key)
        return 1 + self.measure_distance(node.right, key)


    def display(self, node):
        if not node:
            return 
        self.display(node.left)
        print(node.data, end=' ')
        self.display(node.right)


# Main drive :
tree = BinarySearchTree()
n = int(input())
for _ in range(n):
    tree.root = tree.insert(tree.root, int(input()))
source = int(input())
dest = int(input())
# Output stream :
lca = tree.find_common_ancestor(tree.root, source, dest)
source_distance = tree.measure_distance(lca, source)
dest_distance = tree.measure_distance(lca, dest)
print(source_distance + dest_distance)
