class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.stack_size = 0

    def push(self, option, value):
        if self.stack_size < option: 
            new_node = Node(value)
            if self.head is not None:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            self.stack_size += 1
            return "PUSH " + str(value) + " SUCCESSFUL"
        return "Stack overflow"

    def peek(self):
        if self.stack_size <= 0:
            return "STACK EMPTY"
        return self.head.data

    def pop(self):
        if not self.head: 
            return "Stack underflow" 
        element = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self.stack_size -= 1
        return "POP " + str(element)

# Input stream
N = int(input())
stack = DLL()
while True:
    option = list(map(int, input().split()))
    if option[0] == 1:
        print(stack.push(N, option[1]))
    elif option[0] == 2:
        print(stack.pop())
    elif option[0] == 3:
        print(stack.peek())
    elif option[0] == 4:
        break
