# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0

        def dfs(node, max_curr, min_curr):
            if node:
                self.res = max(self.res, abs(node.val - max_curr), abs(node.val - min_curr))
                max_curr = max(max_curr, node.val)
                min_curr = min(min_curr, node.val)
                dfs(node.left, max_curr, min_curr)
                dfs(node.right, max_curr, min_curr)

        dfs(root, root.val, root.val)
        return self.res


"""
Approach:

Find maximum and minimum element so far while dfs at each node and find max difference
at each node.
 
"""