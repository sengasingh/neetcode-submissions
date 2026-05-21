# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p,q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node is None and q_node is None:
                continue
            
            if p_node is None or q_node is None:
                return False

            if p_node.val != q_node.val:
                return False
            
            stack.append((p_node.right, q_node.right))
            stack.append((p_node.left, q_node.left))
        
        return True