class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, val):
        node = Node(val)
        if self.head == None: 
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            past = current.next
            current.next = prev
            prev = current
            current = past
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()

# Input stream :
n = int(input())
dump = [int(input()) for _ in range(n)]
sll = LinkedList()
# Inserting :
for num in dump:
    sll.insert(num)
# Displaying :
sll.reverse()
sll.display()

