# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def dfs(root, path=""):
            if not root:
                return
            elif not root.left and not root.right:
                paths.append(path + str(root.val))
            else:
                dfs(root.left, path + f'{root.val}->')
                dfs(root.right, path + f'{root.val}->')
        
        dfs(root)
        return paths