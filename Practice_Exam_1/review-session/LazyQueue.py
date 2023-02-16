class Node:
    def __init__(self, value):
        self._next = None
        self._prev = None
        self._value = value


class lazyQueue:
    def __init__(self, items=None):
        self._head = None
        self._tail = None
        self._shadow_tail = None
        self._len = 0
        self._actual_len = 0

        if items is not None:
            for item in items:
                self.enqueue(item)
    
    def enqueue(self, value):
        if self._head is None:
            self._head = Node(value)
            self._tail = self._head

        else:
            new_node = Node(value)
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node
    
    def dequeue(self, value):
        self._len -= 1
        if self._len / self._actual_len < .5:
            value = self._shadow_tail.value
            next = self._shadow_tail._next 
            while next is not None:
                next = next._next
                del next.prev
            self._tail = self._shadow_tail

            #delete Nodes
            self._actual_len = self._len
        else:
            self._shadow_tail = self._shadow_tail._prev
            value = self._shadow_tail._prev.value

    def __len__(self):
        return self._len