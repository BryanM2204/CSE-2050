class Node:
    def __init__(self, item, _next):
        self.item = item
        self._next = _next

    def __repr__(self):
        return f'Node({self.item})'

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def add_first(self, item):
        #Edge case - adding the first ndoe to an empty ll
        """
        if len(self) == 0:
           # new_node = Node(item, _next=None)
            #self._head = new_node
            self._tail = new_node
           # self._len += 1
        """

        #General case - adding to a LL that has a few nodes already
        new_node = Node(item, _next=self._head)
        self._head = new_node
        self._len += 1

        if len(self) == 1:
            self._tail = self._head

    def remove_first(self):
        #Edge case - removing the last item
                    
        #general case - removign form an ll w/ a fwe nodes

        #extract item to return
        item = self._head.item
        #update head pointer
        self._head = self._head._next
        #decrement length
        self._len -= 1

        if len(self) == 0:
            self._tail = self._head

        return item


    def __len__(self):
        return self._len