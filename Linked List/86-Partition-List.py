# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        more = ListNode()

        ptr1, ptr2, curr = less, more, head

        while curr:
            if curr.val < x:
                ptr1.next = curr
                ptr1 = ptr1.next
            else:
                ptr2.next = curr
                ptr2 = ptr2.next
            curr = curr.next

        ptr1.next = more.next # join the lists
        ptr2.next = None      # cuts the end of the list to prevent cycle 

        return less.next 
    
    
"""
Approach: Create two linked list and join them

"""