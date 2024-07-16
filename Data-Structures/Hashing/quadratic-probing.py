class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        i = 0
        while self.hash_table[(index + i*i) % self.size] is not None:
            i += 1
            if i == self.size:
                return 'Error!!'
        self.hash_table[(index + i*i) % self.size] = key

    def display(self):
        for i, key in enumerate(self.hash_table):
            print(f"index {i} value = {key}")

# Input Stream :
N = int(input())
if N > 0:
    hash_table = QuadraticProbingHashTable(N)
    array = list(map(int, input().split()))
    for key in array:
        hash_table.insert(key)

hash_table.display()

