# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: # Both of them are leaf nodes
            return True
        if p == None or q == None: # One of them is a leaf node and the other is not. Hence false
            return False
        if p.val == q.val: # Val of both nodes is equal
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Approach: DFS recursive

"""