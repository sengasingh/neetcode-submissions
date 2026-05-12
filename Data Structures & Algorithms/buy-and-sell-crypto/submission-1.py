class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, best = 0, 0
        for r, price in enumerate(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                while l < r and prices[r] - prices[l] < 0:
                    l += 1
            else:
                best = max(best, diff)

        return best