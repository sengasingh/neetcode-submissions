from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        t_counts = Counter(t)
        needed = set(t_counts.keys())

        s_counts = {}
        for key in t_counts.keys():
            s_counts[key] = 0

        l, best = 0, [-1,-1,len(s)+1]
        for r, char in enumerate(s):
            if char in s_counts:
                s_counts[char] += 1

                if s_counts[char] >= t_counts[char]:
                    needed.discard(char)
            
            print(f'{s[best[0]:best[1]+1]}, needed: {needed}, r: {r}')
            while not needed:
                if r-l+1 < best[2]:
                    best = [l,r,r-l+1]
                
                l_char = s[l]
                if l_char in s_counts:
                    s_counts[l_char] -= 1

                    if s_counts[l_char] < t_counts[l_char]:
                        needed.add(l_char)

                l += 1

        if best[2] == len(s)+1:
            return ''

        return s[best[0]:best[1]+1]
