class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        return

    def insert_between(self, value, position):
        new_node = Node(value)
        fast = self.head
        slow = None
        while position - 1 != 0:
            slow = fast
            fast = fast.next
            position -= 1
        new_node.next = fast
        fast.prev = new_node
        slow.next = new_node
        new_node.prev = slow
        return

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        return

    def delete(self, del_val):
        temp = self.head
        prev = None
        while del_val - 1 != 0:
            prev = temp
            temp = temp.next
            del_val -= 1
        prev.next = temp.next
        temp.next.prev = temp.prev
        return

# Input stream :
obj = DLL()
# Adding elements:
for _ in range(3):
    obj.insert(int(input()))
# Inserting at position 2:
k = int(input())
obj.insert_between(k, 2)
# Deleting the specific position:
obj.delete(3)
obj.display()



