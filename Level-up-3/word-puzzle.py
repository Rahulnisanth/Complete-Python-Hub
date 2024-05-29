puzzle = [
    ['A','B','C','I'],
    ['B','I','C','S'],
    ['C','D','E','E']
]

def solve_puzzle(word) -> bool:
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            # Traversing all the indices :
            if(find_word(i, j, 0, word)): return True
    return False

def find_word(i, j, idx, search_word) -> bool:
    # Edge cases / Invalid points :
    if(i < 0 or i >= len(puzzle) or j < 0 or j >= len(puzzle[i])): return False
    # If letter doesn't matched :
    if(puzzle[i][j] != search_word[idx]): return False
    # If idx reached end / All letters found :
    if(idx == len(search_word) - 1): return True
    # Mark as visited :
    puzzle[i][j] = '#'
    found = find_word(i, j + 1, idx + 1, search_word) or find_word(i, j - 1, idx + 1, search_word) or find_word(i + 1, j, idx + 1, search_word) or find_word(i - 1, j, idx + 1, search_word) 
    # Un-mark the letter :
    puzzle[i][j] = search_word[idx]
    return found

t = int(input())
for _ in range(t):
    search_word = input()
    print(solve_puzzle(search_word))

