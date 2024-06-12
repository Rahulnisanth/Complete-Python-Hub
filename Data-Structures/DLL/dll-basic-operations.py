class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
        return 
    
    def insert(self, head, value):
        node = Node(value)
        node.next = head
        node.prev = None
        if head:
            head.prev = node
        return node

# Input stream :
head = None
dll = DoubleLinkedList()
array = list(map(int, input().split()))
for num in array:
    dll.insert(head, num)
dll.display(head)