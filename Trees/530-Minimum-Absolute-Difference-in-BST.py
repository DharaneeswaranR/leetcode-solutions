# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minimum = 99999
        prev = None

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nonlocal prev, minimum
            if prev != None:
                minimum = min(minimum, root.val - prev)
            prev = root.val
            inorder(root.right)

        inorder(root)
        return minimum


"""
Approach:

We have to use inorder traversel at the tree is BST and to minimize the difference we find the
difference between to consecutive inorder nodes

"""