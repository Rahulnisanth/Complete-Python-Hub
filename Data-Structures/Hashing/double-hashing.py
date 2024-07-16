class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def primary_hash(self, key):
        return key % self.size

    def secondary_hash(self, key):
        return 7 - (key % 7)  

    def insert(self, key):
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        original_index = index
        while self.hash_table[index] is not None:
            index = (index + step_size) % self.size
            if index == original_index:
                return 'None'
        self.hash_table[index] = key

    def display(self):
        for i, key in enumerate(self.hash_table):
            print(f"index {i} value = {key}")

# Input Stream :
N = int(input())
if N > 0:
    hash_table = DoubleHashingHashTable(N)
    array = list(map(int, input().split()))
    for key in array:
        hash_table.insert(key)

hash_table.display()

