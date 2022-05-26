# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = None
        curr = front = head
        
        while front:
            front = front.next
            curr.next = prev
            prev = curr
            curr = front
            
        return prev


"""
Approach: Three pointers

1 -> 2 -> 3 -> 4 -> 5
^    ^    ^
pt1  pt2  pt3

"""