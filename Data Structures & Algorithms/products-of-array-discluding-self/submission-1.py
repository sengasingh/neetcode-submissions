class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        to_left, to_right = [1]*n, [1]*n

        for i in range(n-1):
            to_left[i+1] = to_left[i] * nums[i]
        
        for i in range(n-1,0,-1):
            to_right[i-1] = to_right[i] * nums[i]
        
        return [to_left[i]*to_right[i] for i in range(n)]