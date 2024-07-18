class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash(key)
        self.hash_table[idx].append(key)

    def display(self):
        for i, values in enumerate(self.table):
            if values:
                print(f"at index {i}")
                for key in values:
                    print(f"{key}->", end='')
                print()
            else:
                print(f"at index {i}")
                print("No Hash Entry")


# Input Stream :
N = int(input())
if N > 0:
    hash_table = SeparateChainingHashTable(N)
    array = list(map(int, input().split()))
    for key in array:
        hash_table.insert(key)

hash_table.display()

