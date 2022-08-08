# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = deque([])
        prev = None
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            if prev and prev.val >= node.val:
                return False
            prev = node
            root = node.right
            
        return True


"""
Approach: Iterative Inorder Traversal

Traverse the tree using iterative inorder and check if previous node is less than current node. 

"""