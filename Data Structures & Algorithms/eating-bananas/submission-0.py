class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def willFinish(rate: int) -> bool:
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/rate)
                if hrs > h:
                    return False
            
            return True
        
        l, r, best = 1, max(piles), -1
        while l <= r:
            mid = (l+r)//2
            if willFinish(mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return best