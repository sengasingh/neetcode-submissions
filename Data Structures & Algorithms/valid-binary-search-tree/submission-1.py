# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, _min, _max = stack.pop()
            if not _min < node.val < _max:
                return False
            
            if node.right:
                stack.append((node.right, node.val, _max))
            
            if node.left:
                stack.append((node.left, _min, node.val))
        
        return True