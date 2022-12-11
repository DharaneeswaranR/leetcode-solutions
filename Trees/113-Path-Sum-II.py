# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(root, path_sum, path):
            if not root:
                return
            if not root.left and not root.right and path_sum + root.val == targetSum:
                paths.append(path + [root.val])
            dfs(root.left, path_sum + root.val, path + [root.val])
            dfs(root.right, path_sum + root.val, path + [root.val])

        dfs(root, 0, [])
        return paths

