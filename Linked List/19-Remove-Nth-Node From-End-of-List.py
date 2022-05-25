# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = ListNode()
        slow.next = fast.next = head
        
        res = slow
        
        for i in range(n):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return res.next
        
"""
Approach:

Create two pointers slow and fast with a dummy node with next pointing to head. 
Move the fast pointer "n" steps forward then move both slow and fast pointes together
till fast pointer reaches the end. Now slow pointer is pointing to the previous node of
the node to be removed. Now simply change next pointer to point the next node after node to
be removed.

"""