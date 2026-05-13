class Solution:
    def isValid(self, s: str) -> bool:
        pairings = {')':'(', ']':'[','}':'{'}
        stack = []

        for char in s:
            if char in pairings:
                if not stack or stack and stack[-1] != pairings[char]:
                    return False
                
                stack.pop()
            else:
                stack.append(char)
            
        return not stack