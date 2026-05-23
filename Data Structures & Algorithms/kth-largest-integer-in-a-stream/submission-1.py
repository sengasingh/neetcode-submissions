import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.capacity = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.capacity:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heapreplace(self.minHeap, val)
        
        return self.minHeap[0]
