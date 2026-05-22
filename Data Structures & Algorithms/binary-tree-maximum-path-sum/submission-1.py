# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _max = float('-inf')
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal _max
            if not node:
                return float('-inf')
            
            left = dfs(node.left)
            right = dfs(node.right)

            _max = max(left, right, left+node.val, right+node.val,
            left+right+node.val, node.val, _max)

            return max(left+node.val, right+node.val, node.val)
        
        dfs(root)
        return _max