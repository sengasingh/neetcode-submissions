# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: Optional[TreeNode], largest: int) -> int:
            if node is None:
                return 0

            good_node = 0
            if node.val >= largest:
                good_node = 1
            
            left = dfs(node.left, max(largest, node.val))
            right = dfs(node.right, max(largest, node.val))

            return left + right + good_node
        
        return dfs(root, float('-inf'))