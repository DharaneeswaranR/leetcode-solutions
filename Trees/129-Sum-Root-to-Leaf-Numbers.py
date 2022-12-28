# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root, val):
            if root:
                val = val * 10 + root.val
                if not root.left and not root.right:
                    self.res += val
                dfs(root.left, val)
                dfs(root.right, val)
        
        dfs(root, 0)
        return self.res
        

"""
Approach: Recurcive DFS

Keep track of the number at each nodes and add it to the sum variable if the current node
is a leaf node.

"""