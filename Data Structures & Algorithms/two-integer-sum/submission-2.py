class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [seen[rem], i]
            else:
                seen[num] = i
