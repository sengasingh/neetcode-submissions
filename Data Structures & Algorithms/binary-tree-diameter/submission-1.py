# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            best = max(best, left+right, left, right, 0)
            return 1 + max(left, right, 0)
        
        dfs(root)
        return best
