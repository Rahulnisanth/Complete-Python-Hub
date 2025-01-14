# KTH LARGEST ELEMENT IN THE ARRAY :
import heapq
def findKthLargest(nums, k) -> int:
    if not nums:
        return 
    heap = [heapq.heappush(heap, num) for num in nums]
    while len(heap) > k:
        heapq.heappop(heap)
    return heap[0]


# SMALLEST ELEMENT IN THE INFINITE SET :
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.current_smallest = 1
        self.removed = []
        self.added_back = set()

    def popSmallest(self) -> int:
        if self.removed:
            smallest = heapq.heappop(self.removed)
            self.added_back.remove(smallest)
            return smallest
        else:
            self.current_smallest += 1
            return self.current_smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.current_smallest and num not in self.added_back:
            heapq.heappush(self.removed, num)
            self.added_back.add(num)


# TOTAL COST TO HIRE K WORKERS :
def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    totalCost, N = 0, len(costs)
    Lheap = costs[:candidates]
    heapq.heapify(Lheap)
    Rheap = costs[max(candidates, N - candidates) :]
    heapq.heapify(Rheap)
    left, right = candidates, N - candidates - 1
    while k > 0:
        if Lheap and Rheap:
            if Lheap[0] <= Rheap[0]:
                totalCost += heapq.heappop(Lheap)
                if left <= right:
                    heapq.heappush(Lheap, costs[left])
                    left += 1
            else:
                totalCost += heapq.heappop(Rheap)
                if left <= right:
                    heapq.heappush(Rheap, costs[right])
                    right -= 1

        elif Lheap:
            totalCost += heappop(Lheap)

        elif Rheap:
            totalCost += heappop(Rheap)

        k -= 1

    return totalCost
