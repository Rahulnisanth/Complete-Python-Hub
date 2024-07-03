from collections import deque
def rearrange_cards(deck, N) -> list:
    deck.sort()
    result = [0] * N
    indices = deque()
    for i in range(N):
        indices.append(i)
    # Main play :
    for card in deck:
        idx = indices.popleft()
        result[idx] = card
        if indices: 
            indices.append(indices.popleft())
    return result

# Input stream :
N = int(input())
deck = [int(input()) for _ in range(N)]
print(f"result:{rearrange_cards(deck, N)}")