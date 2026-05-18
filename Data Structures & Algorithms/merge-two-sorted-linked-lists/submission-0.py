# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        dummy, ptr1, ptr2 = ListNode(0), list1, list2
        ptr = dummy
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            
            ptr = ptr.next
        
        if ptr1:
            ptr.next = ptr1
        
        if ptr2:
            ptr.next = ptr2
        
        return dummy.next