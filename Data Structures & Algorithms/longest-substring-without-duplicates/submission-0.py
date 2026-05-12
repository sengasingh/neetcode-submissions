class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett, l, best = set(), 0, 0
        for r, char in enumerate(s):
            if char in sett:
                while l < r and s[l] != s[r]:
                    sett.discard(s[l])
                    l += 1

                l += 1

            sett.add(char)
            best = max(best,(r-l)+1)

        return best