class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        i = 0
        while self.hash_table[(index + i * i) % self.size] is not None:
            print(f"Inserting {key} in index {(index + i * i) % self.size} -> Collision")
            i += 1
        idx = (index + i * i) % self.size
        print(f"Inserting {key} in index {idx}")
        self.hash_table[idx] = key

    def display(self):
        print("\nHash table:")
        for i, key in enumerate(self.hash_table):
            print(f"Element at position {i}: {key}")

# Input Stream :
N = int(input())
if N > 0:
    hash_table = QuadraticProbingHashTable(N + (N//2))
    array = list(map(int, input().split()))
    for key in array:
        hash_table.insert(key)

hash_table.display()

