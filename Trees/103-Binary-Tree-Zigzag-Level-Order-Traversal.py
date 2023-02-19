# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zig = []
        deq = deque([root])
        flag = False

        while deq:
            level = []
            for i in range(len(deq)):
                if flag:
                    node = deq.pop()
                    if node.right:
                        deq.appendleft(node.right)
                    if node.left:
                        deq.appendleft(node.left)
                    level.append(node.val)
                else:
                    node = deq.popleft()
                    if node.left:
                        deq.append(node.left)
                    if node.right:
                        deq.append(node.right)
                    level.append(node.val)
            zig.append(level)
            flag = not flag

        return zig