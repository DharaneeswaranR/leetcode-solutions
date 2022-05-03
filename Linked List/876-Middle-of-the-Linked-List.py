# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My initial approach
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        mid = curr = head
        
        while curr:
            curr = curr.next
            count += 1
            
        for i in range(count // 2):
            mid = mid.next
            
        return mid

# A better approach
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow


"""
Approach: Two pointers

Create two pointers slow and fast. Move slow ptr 1 step and fast ptr
2 steps, so that when fast ptr reaches end of the LL, the slow ptr
will be at the mid.

"""