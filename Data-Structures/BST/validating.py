class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert_level_order(self, values):
        if not values:
            return None
        
        self.root = Node(values[0])
        nodes = [self.root] 
        for i in range(1, len(values)):
            new_node = Node(values[i])
            parent_index = (i - 1) // 2 
            if i % 2 == 1:  
                nodes[parent_index].left = new_node
            else:  
                nodes[parent_index].right = new_node
            nodes.append(new_node)  
    
    def is_valid(self, node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (self.is_valid(node.left, min_val, node.data) and
                self.is_valid(node.right, node.data, max_val))

# Main driver:
tree = BinarySearchTree()
inputs = [int(input()) for _ in range(7)]  
tree.insert_level_order(inputs)

if tree.is_valid(tree.root):
    print("Valid BST")
else:
    print("Invalid BST")

