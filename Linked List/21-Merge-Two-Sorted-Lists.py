# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = new = ListNode() # dummy node
        curr1 = list1
        curr2 = list2
        
        while curr1 or curr2: 
            if not curr1: # end of list 1 -> attach remaining of list 2 at the end
                ptr.next = curr2
                return new.next
                
            if not curr2: # end of list 2 -> attach remaining of list 1 at the end
                ptr.next = curr1
                return new.next
                
            if curr1.val > curr2.val:
                ptr.next = curr2
                curr2 = curr2.next
                
            else: 
                ptr.next = curr1
                curr1 = curr1.next

            ptr = ptr.next
                
        return new.next