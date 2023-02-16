class LLNode:
    def __init__(self, item, _next):
        self.item = item
        self._next = _next
    
    def __repr__(self):
        return f'LLNode({self.item})'

class LinkedList:
    def __init__(self, items=None):
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)

    def add_last(self, item):
        new_node = LLNode(item, _next=None)

        #if this is the first node
        if len(self) == 0:
            self._head = new_node
        else:
            self._tail._next = new_node

        self._tail = new_node

        self._len += 1

    def remove_last(self, item):
        if len(self) == 0:
            raise RuntimeError('Can not remove from empty linked list')
        
        item = self._tail.item

        penultimate = self._head
        if len(self) > 1:
            while penultimate._next._next is not None:
                penultimate = penultimate._next

            penultimate._next = None

            self._tail = penultimate
        else:
            self._head = None
            self._tail = None

        self._len -= 1

        return item

    def __len__(self): return self._len