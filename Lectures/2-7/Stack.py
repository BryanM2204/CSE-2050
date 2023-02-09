class Stack:
    'Wrapper pattern - list wrapper'

    def __init__(self):
        self._L = [] # leading underscore - 'private' attribute

    def push(self, item):
        self._L.append(item) #O(1)
        self._L.insert(0, item)

    def pop(self):
        return self._L.pop() #O(1)
        return self._L.pop(0)

class Queue:
    def __init__(self):
        self._Q = []

    def enqueue(self, item):
        self._Q.append(item) #O(1)

    def dequeue(self):
        return self._Q.pop(0) #O(n)

#BAD WAY TO DO A STACK
import time
class StackSet:
    'warpper pattern - set wrapper'

    def __init__(self):
        self._S = set()

    def push(self, item):
        new_item = (time.time(), item)
        self._S.add(new_item)
        time.sleep(0.01)

    def pop(self):
        t_max = 0
        for item_tup in self._S:
            if item_tup[0] > t_max:
                t_max = item_tup[0] #now my most recent item
                oldest_item = item_tup

        self._S.remove(oldest_item)
        return oldest_item[1]