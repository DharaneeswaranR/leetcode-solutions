# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        
        curr = root
        
        while curr:
            prev = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        
        if val > prev.val:
            prev.right = TreeNode(val, None, None)
        else:
            prev.left = TreeNode(val, None, None)
            
        return root
    
        
# Recursive solution
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root