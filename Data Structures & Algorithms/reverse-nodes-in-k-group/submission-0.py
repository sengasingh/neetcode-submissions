# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        anchor, scout = dummy, dummy

        while True:
            for _ in range(k):
                scout = scout.next
                if scout is None:
                    return dummy.next
            
            curr = anchor.next
            for _ in range(k-1):
                _next = curr.next
                curr.next = _next.next
                _next.next = anchor.next
                anchor.next = _next
            
            anchor = curr
            scout = curr
        
        return dummy.next