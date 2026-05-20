# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))
        
        dummy = ListNode(0)
        ptr = dummy

        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            ptr.next = node
            ptr = ptr.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, idx, node.next))
            
        return dummy.next