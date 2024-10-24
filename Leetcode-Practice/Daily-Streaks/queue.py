from collections import deque


class MyCircularDeque:
    def __init__(self, k: int):
        self.q = deque(maxlen=k)
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return True if len(self.q) <= 0 else False

    def isFull(self) -> bool:
        return True if len(self.q) == self.k else False


# THE NUMBER OF SMALLEST UNOCCUPIED CHAIRS :
import heapq


def smallestChair(times, targetFriend: int) -> int:
    chair, temp, target = 0, 0, times[targetFriend]
    chair_taken, chair_free = [], []
    times = sorted(times, key=lambda x: x[0])
    for start, end in times:
        while chair_taken and chair_taken[0][0] <= start:
            heapq.heappush(chair_free, heapq.heappop(chair_taken)[1])
        if chair_free:
            temp = heapq.heappop(chair_free)
            heapq.heappush(chair_taken, [end, temp])
        else:
            temp = chair
            heapq.heappush(chair_taken, [end, chair])
            chair += 1
        if start == target[0]:
            return temp
    return -1


# MAXIMUM SCORE AFTER APPLYING K OPERATIONS :
import math


def maxKelements(nums, k) -> int:
    heap = [-num for num in nums]
    heapq.heapify(heap)
    score = 0
    for _ in range(k):
        item = -heapq.heappop(heap)
        score += item
        heapq.heappush(heap, -math.ceil(item / 3))
    return score
