# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
        if root1:
            return root1
        if root2:
            return root2

        return root1
    
"""
Aprroach:

1. If both the nodes are not null, then add the values of both the nodes and store it in the root1 node.
2. Now, recursively call the mergeTrees function for the left and right nodes of the root1 node.
3. If only one node is not null simply return that node.

Time Complexity: O(n)

"""