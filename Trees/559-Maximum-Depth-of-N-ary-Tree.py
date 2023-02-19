"""
# Definition for a Node.
class Node:
def __init__(self, val=None, children=None):
self.val = val
self.children = children
"""

# Recusive DFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0

        for child in root.children:
            depth = max(depth, self.maxDepth(child))

        return depth + 1

# Iterative DFS using Stack
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        stack = deque([[root, 1]])
        depth = 0

        while stack:
            node, d = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append([child, d+1])

        return depth

# BFS using Queue
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            depth += 1

        return depth


