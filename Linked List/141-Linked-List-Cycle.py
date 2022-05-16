# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Floyd loop - Two pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:       
        if not head:
            return False
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False

# Hashing
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        
        while head:
            if head in hashset:
                return True
            hashset.add(head)
            head = head.next
            
        return False


"""
Explanation: Floyd loop detection

Create two pointers slow and fast. For every one step slow pointer moves, fast pointer moves two steps.
The one way fast pointer meets slow pointer is that if the linkedlist containes loop.

"""