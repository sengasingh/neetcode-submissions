from collections import defaultdict
import heapq
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap, counts = [], defaultdict(int)
        for num in nums:
            if num not in counts:
                if len(minHeap) < k:
                    heapq.heappush(minHeap, num)
                elif num > minHeap[0]:
                    heapq.heapreplace(minHeap, num)
            
            counts[num] += 1

        minHeap.sort(key=lambda x: -x)
        for num in minHeap:
            k -= counts[num]
            if k <= 0:
                return num
        
        return -1
