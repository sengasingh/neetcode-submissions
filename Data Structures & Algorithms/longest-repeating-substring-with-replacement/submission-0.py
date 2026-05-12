from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, counts, best = 0, defaultdict(int), 0
        
        for r, char in enumerate(s):
            counts[char] += 1
            while r-l+1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            best = max(best, r-l+1)
        
        return best