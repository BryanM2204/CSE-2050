class Node:
    'node for dll classes'
    def __init__(self, item, _next, _prev):
        'constructs a new node'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        return f'Node({self.item})'

class DoublyLinkedList:
    def __init__(self):
        'constructs a new (empty) dll'
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        'returns the number of items in dll'
        return self._len

    def add_first(self, item): 
        #general case

        #create a new node, pointed to ehad
        new_node = Node(item, _next=self._head, _prev=None)

        #update old head's prepointer
        if len(self) > 0: self._head._prev = new_node
        else: self._tail = new_node

        #update head
        self._head = new_node

        #incrememnt length
        self._len += 1

    def remove_last(self, item):
        #General case

        #extract item from tail
        temp_item = self._tail.item

        #update penultimate node ._next
        if len(self) > 1: self._tail._prev._next = None
        else: self._head = None

        #update self._tail
        self._tail = self._tail._prev

        #decrement length
        self._len -= 1

        if len(self) == 0:
            self._head = None

        #return item
        return temp_item


    def add_last(self, item): 
            #general case

            #create a new node, pointed to ehad
            new_node = Node(item, _next=None, _prev=self._tail)

            #update old head's prepointer
            if len(self) > 0: self._tail._next = None
            else: self._head = new_node

            #update head
            self._tail = new_node

            #incrememnt length
            self._len += 1


    def remove_first(self): 
        #General case

        #extract item from tail
        temp_item = self._head.item

        #update penultimate node ._next
        if len(self) > 1: self._head._next._prev = None
        else: self._tail = None

        #update self._tail
        self._head = self._head._next

        #decrement length
        self._len -= 1

        if len(self) == 0:
            self._head = None

        #return item
        return temp_item