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

print(kthsmallestprimefraction([1,2,3,5],3))
