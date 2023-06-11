# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = front = head

        while front:
            front = front.next
            curr.next = prev
            prev = curr
            curr = front
        
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        second = head
        for i in range(length // 2):
            second = second.next
        
        second_head = self.reverse(second)

        min_sum = 0
        while second_head:
            min_sum = max(min_sum, head.val + second_head.val)
            head = head.next
            second_head = second_head.next
        
        return min_sum
