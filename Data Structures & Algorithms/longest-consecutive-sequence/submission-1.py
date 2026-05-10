class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett, best = set(nums), 0

        for num in nums:
            if num-1 not in sett:
                curr, count = num, 0
                while curr in sett:
                    count += 1
                    sett.discard(curr)

                    curr += 1
            
                best = max(best, count)

        return best