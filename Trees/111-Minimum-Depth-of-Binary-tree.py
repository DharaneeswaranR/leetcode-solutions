# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS Approach (Recommended)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                
                if not node.left and not node.right: # if is a leaf node return depth
                    return level + 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1


# DFS Approach
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if not root.left or not root.right: 
            return max(1 + l, 1 + r)
        else:
            return min(1 + l, 1 + r)


"""
Approach:

1) BFS (level order)
    The depth of the first leaf node in bfs (level order) traversal is the minimum depth. 
Keep track of level during bfs and return the current level if the node is a leaf node.

2) DFS
    This approach is similar to recursive dfs used to find 104-Maximum-Depth-of-Binary-Tree.
The only difference is we have to find min depth at each node recursively.
    Edge case: If the node has both left and right child we should return min depth at that 
node, else return max depth at that node (ie depth from left or right closest leaf node).
   
"""