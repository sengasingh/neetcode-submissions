class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        width, stack = [1]*n, [] # [ (height, index) ]

        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            if stack:
                width[i] = stack[-1][1] - i
            else:
                width[i] = n - i
            
            stack.append([heights[i],i])
        
        stack.clear()
        for i in range(n):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            # -1 so that cuz idx's single-width already accounted for in prev loop
            if stack:
                width[i] += (i - stack[-1][1]) - 1
            else:
                width[i] += (i + 1) - 1
            
            stack.append([heights[i],i])

        return max([width[i]*heights[i] for i in range(n)])

