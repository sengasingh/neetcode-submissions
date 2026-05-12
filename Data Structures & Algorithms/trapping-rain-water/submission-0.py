class Solution:
    def trap(self, height: List[int]) -> int:
        n, stack = len(height), []
        max_to_left, max_to_right = [0]*n, [0]*n

        for i, num in enumerate(height):
            while stack and stack[-1] <= num:
                stack.pop()
            
            if stack:
                max_to_left[i] = stack[-1]
            else:
                stack.append(num)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= height[i]:
                stack.pop()
            
            if stack:
                max_to_right[i] = stack[-1]
            else:
                stack.append(height[i])

        total = 0
        for i in range(n):
            diff = min(max_to_left[i],max_to_right[i]) - height[i]
            if diff > 0:
                total += diff
        
        return total