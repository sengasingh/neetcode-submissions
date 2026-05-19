# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr, n = head, 0
        while ptr:
            n += 1
            ptr = ptr.next
        
        steps = n//2 - 1 if n%2==0 else n//2
        ptr = head
        for _ in range(steps):
            ptr = ptr.next
        
        head2 = ptr.next
        ptr.next = None

        prev, curr = None, head2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head2 = prev

        dummy = ListNode(0)
        ptr = dummy
        ptr1, ptr2 = head, head2

        while ptr1 and ptr2:
            ptr.next = ptr1
            ptr1 = ptr1.next
            ptr = ptr.next

            ptr.next = ptr2
            ptr2 = ptr2.next
            ptr = ptr.next
        
        if ptr1:
            ptr.next = ptr1
        
        head = dummy.next