import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-stone for stone in stones]
        heapq.heapify(minHeap)

        while len(minHeap) >= 2:
        
            x = -heapq.heappop(minHeap)
            y = -heapq.heappop(minHeap)

            if x == y:
                continue
            
            z = max(x,y) - min(x,y)
            heapq.heappush(minHeap, -z)
        
        return 0 if len(minHeap) == 0 else -minHeap[0]