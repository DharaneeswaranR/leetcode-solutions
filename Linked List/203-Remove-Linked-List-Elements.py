# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        res = prev = ListNode() # dummy node pointing head node as head may need to be deleted
        res.next = prev.next = head
        
        while curr:
            if curr.val == val:
                prev.next = prev.next.next
            else:
                prev = curr
            curr = curr.next
            
        return res.next