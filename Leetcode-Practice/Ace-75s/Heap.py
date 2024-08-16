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
