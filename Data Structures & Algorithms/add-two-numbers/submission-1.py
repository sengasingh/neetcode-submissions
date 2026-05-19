# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr, carry = dummy, 0

        ptr1, ptr2 = l1, l2
        while ptr1 or ptr2:
            dig1 = 0 if not ptr1 else ptr1.val
            dig2 = 0 if not ptr2 else ptr2.val

            total = dig1+dig2+carry
            ptr.next = ListNode(total%10)
            ptr = ptr.next

            carry = total//10 if total > 9 else 0
            
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        
        if carry > 0:
            ptr.next = ListNode(carry)

        return dummy.next