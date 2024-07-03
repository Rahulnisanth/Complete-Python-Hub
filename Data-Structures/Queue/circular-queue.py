class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueGame:
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        self.size += 1
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            tail.next = new_node
            new_node.next = self.head

    def play_game(self, count):
        if self.size == 0:
            print("No elements in queue")
            return None
        slow = None
        fast = self.head
        for _ in range(count - 1):
            slow = fast
            fast = fast.next
        slow.next = fast.next
        # Updating the next node as the head :
        self.head = fast.next
        self.size -= 1
        return fast.data

    def starter(self, value):
        while self.size > 1:
            removed_data = self.play_game(value)
            print(f"Outraged player: {removed_data}")
        if self.head:
            print(f"Winner of the game: {self.head.data}")


# Input stream
queue = CircularQueueGame()
N = int(input("Enter number of elements to insert: "))
for i in range(1, N + 1):
    queue.insert(i)
value = int(input("Enter the game number: "))
queue.starter(value)
