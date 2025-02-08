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


# SHORTEST SUB-ARRAY WITH SUM AT LEAST K
def shortestSubArray(nums, k: int) -> int:
    N = len(nums)
    prefix = [0] * (N + 1)
    # cumulative sum...
    for i in range(N):
        prefix[i + 1] = prefix[i] + nums[i]

    q = deque()
    result = float("inf")
    for i in range(N + 1):
        while q and prefix[i] - prefix[q[0]] >= k:
            result = min(result, i - q.popleft())
        while q and prefix[i] <= prefix[q[-1]]:
            q.pop()
        q.append(i)

    return result if result != float("inf") else -1


# TAKE GIFTS FROM RICHEST PILE
def pickGifts(gifts, k):
    heap = [-gift for gift in gifts]
    heapq.heapify(heap)
    for _ in range(k):
        temp = math.floor(math.isqrt(-heapq.heappop(heap)))
        heapq.heappush(heap, -temp)
    return -sum(heap)     


# CONSTRUCT STRING WITH REPEAT LIMITS
def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        q = [-ord(ch) for ch, _ in counter.items()]
        heapify(q)
        result = []
        while q:
            curr = chr(-heappop(q))
            count = counter[curr]

            if count <= repeatLimit:
                result.append(curr * count)
                del counter[curr]
            else:
                result.append(curr * repeatLimit)
                counter[curr] -= repeatLimit

                if not q:
                    break

                next_char = chr(-heappop(q))
                result.append(next_char)
                counter[next_char] -= 1

                if counter[next_char] > 0:
                    heappush(q, -ord(next_char))
                heappush(q, -ord(curr))

        return "".join(result)


# DESIGN A NUMBER CONTAINER SYSTEM :
class NumberContainers:

    def __init__(self):
        self.numToIdx = {}
        self.idxToNum = {}

    def change(self, index: int, number: int) -> None:
        self.idxToNum[index] = number
        if number not in self.numToIdx:
            self.numToIdx[number] = []
        heappush(self.numToIdx[number], index)

    def find(self, number: int) -> int:
        if number not in self.numToIdx:
            return -1
        q = self.numToIdx[number]
        while q:
            idx = q[0]
            if self.idxToNum[idx] != number:
                heappop(self.numToIdx[number])
            else:
                return idx
        return -1

