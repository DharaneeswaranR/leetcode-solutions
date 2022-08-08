# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque([])
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            popped = stack.pop()
            k -= 1
            if k == 0:
                return popped.val
            
            root = popped.right


"""
Approach: Iterative Inorder Traversal

As inorder traversal gives increasing order of elements, we decrement variable 'k'
to find the kth smallest.

"""