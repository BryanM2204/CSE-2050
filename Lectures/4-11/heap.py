class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f'Entry(item={self.item}, priority={self.priority})'
    
class Heap:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)
    
    def _i_parent(self, idx):
        "returns index of parent of idx"
        return (idx-1) // 2 if (idx-1) // 2 >= 0 else None

    def _i_left(self, idx):
        "left child"

    def _i_right(self, idx):
        "right child"

    def _upheap(self, idx):
        "move item at idx up heap to maintain heap property"
        # find parent idx
        parent = self._i_parent(idx)

        # if parent exists and parent is smaller: swap
        while parent is not None and self._L[parent] > self._L[idx]:
            self._L[parent], self._L[idx] = self._L[idx], self._L[parent]
            # update vars
            idx = parent
            parent = self._i_parent(idx)

    def _downheap(self, idx):
        "move item at idx down heap to maintain heap property"

    def insert(self, item, priority):
        # append entry to list
        # uphead until balanced

        new_e = Entry(item=item, priority = priority)
        self._L.append(new_e)
        self._upheap(len(self) - 1)
    
    def remove_min(self): pass
