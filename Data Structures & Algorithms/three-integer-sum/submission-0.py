class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(l: int, r: int, target: int) -> List[List[int]]:
            res = []
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([l,r])

                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    
                    r -= 1
                    while r > l and nums[r+1] == nums[r]:
                        r -= 1
                    
                elif nums[l] + nums[r] < target:
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                else:
                    r -= 1
                    while r > l and nums[r+1] == nums[r]:
                        r -= 1

            return res
        
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for x,y in twoSum(i+1,len(nums)-1,-nums[i]):
                res.append([nums[i],nums[x],nums[y]])
            
        return res