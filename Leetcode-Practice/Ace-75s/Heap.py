# KTH LARGEST ELEMENT IN ARRAY USING HEAP :
import heapq

def findKthLargest(nums, k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        for _ in range(k):
            result = heapq.heappop(heap)
        
        return -result