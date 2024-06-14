class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.prev = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        
    def display(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

    def dequeue(self):
        if not self.head:
            return "No elements in queue"
        self.head = self.head.next

# Input stream
queue = DLL()
while True:
    option = int(input())
    if option == 1:
        value = int(input())
        queue.enqueue(value)
    elif option == 2:
        queue.dequeue()
    elif option == 3:
        queue.display()
    elif option == 4:
        break
