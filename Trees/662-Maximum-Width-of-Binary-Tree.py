# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 1]])
        max_width = 0

        while queue:
            start, index = queue[0][1], 0

            for i in range(len(queue)):
                node, index = queue.popleft()

                if node.left:
                    queue.append([node.left, index * 2])
                if node.right:
                    queue.append([node.right, index * 2 + 1])

            max_width = max(max_width, index - start + 1)
        
        return max_width

"""
Approach: BFS

-  We will use a queue to store the nodes and their indices as if the nodes are
   represented as an array.
   root - n
   root.left - n * 2
   root.right - n * 2 + 1

- We find the index of the first node and the last node of the level and then
  we will use the difference of these two to find the maximum width.
  
"""