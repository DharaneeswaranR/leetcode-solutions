# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive DFS
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if root: 
                if low <= root.val <= high:
                    ans += root.val
                if low < root.val:
                    dfs(root.left)
                if high > root.val:
                    dfs(root.right)
        
        dfs(root)
        return ans

# Iterative DFS
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = deque([root])

        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if high > node.val:
                    stack.append(node.right)
                
        return ans
