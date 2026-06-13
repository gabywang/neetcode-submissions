# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        head = dummy
        carry = 0

        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            carry, rmd = (v1+v2+carry)//10, (v1+v2+carry)%10
            head.next = ListNode(rmd)
            head = head.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        
        if carry:
            head.next = ListNode(carry)
        
        return dummy.next
