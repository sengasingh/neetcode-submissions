"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapp = {}
        ptr = head

        while ptr:
            mapp[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        dummy = Node(0,next=head)
        ptr, ptr2 = head, dummy

        while ptr:
            ptr2.next = mapp[ptr]
            ptr2 = ptr2.next

            ptr2.random = None if not ptr.random else mapp[ptr.random]

            ptr = ptr.next
        
        return dummy.next
