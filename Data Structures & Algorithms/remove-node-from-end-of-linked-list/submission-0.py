# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        behind, ahead = dummy, dummy

        for _ in range(n):
            ahead = ahead.next
        
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        
        to_del = behind.next
        behind.next = behind.next.next
        to_del.next = None

        return dummy.next