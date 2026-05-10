import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = [(-freq,num) for num, freq in Counter(nums).items()]
        heapq.heapify(minHeap)

        return [heapq.heappop(minHeap)[1] for _ in range(k)]