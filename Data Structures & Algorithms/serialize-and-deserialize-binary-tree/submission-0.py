# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if node is None:
                res.append('N')
                return
            
            res.append(f'{node.val}')
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return '%'.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i, data = 0, data.split('%')
        def build() -> Optional[TreeNode]:
            nonlocal i, data
            if i >= len(data) or data[i] == 'N':
                return None
            
            newNode = TreeNode(int(data[i]))

            i += 1
            newNode.left = build()

            i += 1
            newNode.right = build()

            return newNode

        return build()
