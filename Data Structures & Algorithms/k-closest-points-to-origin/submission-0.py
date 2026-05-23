import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)

            if len(minHeap) < k:
                heapq.heappush(minHeap, (-dist, x,y))
            elif dist < -minHeap[0][0]:
                heapq.heapreplace(minHeap, (-dist, x,y))
            
        return [[x,y] for dist,x,y in minHeap]