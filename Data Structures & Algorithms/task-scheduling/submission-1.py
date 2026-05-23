from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_left = [-freq for _, freq in Counter(tasks).items()]
        heapq.heapify(tasks_left)
        cycle, locked = 0, deque()

        while tasks_left or locked:
            while locked and locked[0][1] <= cycle:
                heapq.heappush(tasks_left, locked.popleft()[0])
            
            if not tasks_left:
                cycle = locked[0][1]
                continue
            
            remaining = heapq.heappop(tasks_left)
            if remaining < -1:
                locked.append((remaining+1, cycle+n+1))
            
            cycle += 1
        
        return cycle