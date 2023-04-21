# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxdepth = 0

        def dfs(node, flip, depth):
            if not node:
                return

            self.maxdepth = max(self.maxdepth, depth)
            if flip:
                dfs(node.left, False, depth+1) # flip to left
                dfs(node.right, True, 1) #  alternative path
            else:
                dfs(node.right, True, depth+1) # flip to right
                dfs(node.left, False, 1) #  alternative path

        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.maxdepth

"""
Approach: DFS

- For each node, we can either go left or right. Hence, we use boolean flip to indicate whether we are going left or right.
- We can also use depth to indicate the length of the path.
- We also check alternative path at each node.

"""