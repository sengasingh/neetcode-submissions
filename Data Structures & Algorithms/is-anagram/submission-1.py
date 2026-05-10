class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_code, t_code = [0]*26, [0]*26

        for i in range(len(s)):
            s_code[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            t_code[ord(t[i]) - ord('a')] += 1
        
        return s_code == t_code