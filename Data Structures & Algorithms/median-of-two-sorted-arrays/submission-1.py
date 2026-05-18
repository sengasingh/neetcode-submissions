class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m

        while l <= r:
            i = (l+r)//2 # smaller arr A partition (how many to take) 
            j = half - i # larger arr B partition (remaining to take) 

            Aleft = A[i-1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')

            Bleft = B[j-1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            if Aleft > Bright: # took too many from A
                r = i - 1
            elif Bleft > Aright: # took too many from B (too few from A)
                l = i + 1
            
            elif max(Aleft,Bleft) <= min(Aright,Bright):
                if (m+n)%2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)