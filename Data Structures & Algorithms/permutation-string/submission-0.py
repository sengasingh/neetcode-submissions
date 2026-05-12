class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        goal = [0]*26
        for char in s1:
            goal[ord(char)-ord('a')] += 1
        
        l, code = 0, [0]*26
        for r, char in enumerate(s2):
            code[ord(char)-ord('a')] += 1

            while r-l+1 > len(s1):
                code[ord(s2[l])-ord('a')] -= 1
                l += 1
            
            if code == goal:
                return True
        
        return False