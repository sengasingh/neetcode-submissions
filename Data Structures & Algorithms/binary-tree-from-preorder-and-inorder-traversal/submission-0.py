# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(_pre: List[int], _in: List[int]) -> Optional[TreeNode]:
            if not _pre or not _in:
                return None
            
            newNode = TreeNode(_pre[0])
            for i, num in enumerate(_in):
                if num == newNode.val:
                    newNode.left = build(_pre[1:i+1], _in[:i])
                    newNode.right = build(_pre[i+1:], _in[i+1:])

                    return newNode
            
            return None
        
        return build(preorder, inorder)