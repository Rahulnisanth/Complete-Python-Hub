# UNREVEALING THE DECK OF CARDS :
from collections import deque
def deckRevealedIncreasing(deck):
    deck.sort()
    n = len(deck)
    result = [0] * n
    indices = deque(range(n))

    for card in deck:
        idx = indices.popleft()
        result[idx] = card
        if indices:
            indices.append(indices.popleft())

    return result


# KTH SMALLEST PRIME FRACTION :
import heapq
def kthsmallestprimefraction(arr, k):
    n = len(arr)
    heap = [(arr[i] / arr[j],arr[i],arr[j]) for i in range(n) for j in range(i + 1, n)]
    heapq.heapify(heap)

    result = None
    for _ in range(k):
        result = heapq.heappop(heap)
    return [int(result[1]), int(result[2])]

