# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

"""
Approach:

- Use two pointers, slow and fast.
- Move slow pointer by one step and fast pointer by two steps.
- If there is a cycle, they will meet at some point.
- Move slow pointer to head.
- Move both pointers one step at a time.
- The meeting point is the entrance of the cycle.

"""