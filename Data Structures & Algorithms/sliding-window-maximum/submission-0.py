from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        biggest = deque() # [(idx,val)]
        res = []

        for i, num in enumerate(nums):

            # remove nums smaller than current (can't be valid)
            while biggest and biggest[-1][1] <= num:
                biggest.pop()

            # remove nums from too long ago
            while biggest and biggest[0][0] <= i - k:
                biggest.popleft()
            
            biggest.append((i,num))

            if i >= k-1:
                res.append(biggest[0][1])
        
        return res