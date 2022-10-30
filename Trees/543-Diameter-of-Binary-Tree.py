# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0] # global scope
    
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            res[0] = max(res[0], left + right)
            
            return max(1 + left, 1 + right)
        
        maxDepth(root)
        
        return res[0]
        

"""
Solution: DFS Approach

The longest path(diameter) can be found by finding the node which has maximum sum of it's
depths of left and right subtrees. The depths of left and right subtrees can be found using
dfs recursively (similar to leetcode 104-Maximum-Depth-of-Binary-Tree).

"""