class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listsum = curr = ListNode()
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            add = v1 + v2 + carry
            curr.next = ListNode(add % 10)
            carry = add // 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
            
        return listsum.next

