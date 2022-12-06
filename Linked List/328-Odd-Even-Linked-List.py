# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_head

        return head
        

"""
Solution: 

Create two pointers pointing first odd and even indices nodes of the list. Attach every odd indexed node with next odd indexed
node and every even indexed node with even indexed node. Finally join both the odd and even lists and return head.

"""

        
