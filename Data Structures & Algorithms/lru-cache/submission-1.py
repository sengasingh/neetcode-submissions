class LRUCache:

    class ListNode:
        def __init__(self,key,val,prev=None,nextt=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.nextt = nextt

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity

        self.mapp = {}

        self.head = None
        self.tail = None
    
    def remove(self,key):
        to_del = self.mapp[key]

        if self.size == 1:
            self.head = self.tail = None
        elif to_del == self.head:
            self.head = self.head.nextt
            to_del.nextt = self.head.prev = None
        elif to_del == self.tail:
            self.tail = self.tail.prev
            to_del.prev = self.tail.nextt = None
        else:
            to_del.prev.nextt = to_del.nextt
            to_del.nextt.prev = to_del.prev

        del self.mapp[key]
        self.size -= 1
        return to_del
    
    def add(self,key,val):
        newNode = self.ListNode(key,val)

        if self.size == 0:
            self.head = self.tail = newNode
        else:
            self.tail.nextt = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        self.mapp[key] = newNode
        self.size += 1
        return newNode

    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1

        _val = self.mapp[key].val

        self.remove(key)
        return self.add(key,_val).val

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.remove(key)
            self.add(key,value)
            return
        
        if self.size == self.capacity:
            self.remove(self.head.key)
        
        self.add(key,value)
        return
