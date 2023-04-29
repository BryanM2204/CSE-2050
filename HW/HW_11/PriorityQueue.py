class Entry:
    def __init__(self, item, priority):
        """Initializes item and priority"""
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        """Returns True if priority of self is less than priority of other"""
        return self.priority < other.priority

    def __repr__(self):
        """Returns string representation of Entry"""
        return f"Entry(item={self.item}, priority={self.priority})"

class Heap:
    def __init__(self):
        """Initializes entries list"""
        self._entries = []

    def __len__(self): 
        """Returns length of entries list"""
        return len(self._entries)

    def _i_parent(self, idx):
        "returns index of parent of idx"
        return (idx-1) // 2 if (idx-1) // 2 >= 0 else None
    
    def _i_left(self, idx):
        "left child"
        il = idx*2+1
        return il if il<len(self) else None
    
    def _i_right(self, idx):
        "right child"
        ir = idx*2+2
        return ir if ir<len(self) else None

    def insert(self, item, priority):
        "adds item w/ given priority to heap"
        # append entry to list
        # upheap until balanced

        new_e = Entry(item=item, priority=priority)
        self._entries.append(new_e)
        self._upheap(len(self)-1)
    
    def _upheap(self, idx):
        "upheaps item at idx"
        # find parent index
        i_p = self._i_parent(idx)

        # while parent exists and parent is bigger: swap
        while i_p is not None and self._entries[i_p] > self._entries[idx]:
            # swap them
            self._entries[i_p], self._entries[idx] = self._entries[idx], self._entries[i_p]
            # update vars for next loop
            idx = i_p
            i_p = self._i_parent(idx)
        
    def peek(self):
        "returns (but does not remove) item with minimum priority"
        return self._entries[0].item
    
    def remove_min(self):
        "removes and returns item with minimum priority"
        # save the item to return
        temp = self._entries[0].item

        # move last item in list to front (top of heap)
        # edge case - one item left
        if len(self) == 1: 
            self._entries.pop()
        else:        
            self._entries[0] = self._entries.pop()

            # downheap until all good
            self._downheap(idx=0)

        # return the temporary variable
        return temp

        
    def _i_min_child(self, idx):
        "returns idx of minimum child if it exists, otherwise None"
        il = self._i_left(idx)
        ir = self._i_right(idx)

        # 0 or 1 children
        if ir is None: return il

        return il if self._entries[il] < self._entries[ir] else ir
        
    def _downheap(self, idx):
        "downheaps item at idx"
        i_min = self._i_min_child(idx)

        while i_min is not None and self._entries[i_min] < self._entries[idx]:
            self._entries[i_min], self._entries[idx] = self._entries[idx], self._entries[i_min]

            # update vars for next loop
            idx = i_min
            i_min = self._i_min_child(idx)
        
class PriorityQueue(Heap):
    """
    PriorityQueue implementation using Heap data structure.
    This class extends Heap and adds functionality to prioritize and sort elements by their priority.
    """

    def __init__(self, items=(), entries=(), key = lambda x: x):
        """Initializes PriorityQueue with items, entries, and key
        items: list of items to be inserted into the PriorityQueue
        entries: list of tuples (item, priority) to be inserted into the PriorityQueue
        key: function that takes an item and returns its priority
        """
        self._key = key
        self._entries = [Entry(i, p) for i, p in entries]
        self._entries.extend([Entry(i, key(i)) for i in items])
        self._itemmap = {entry.item : index for index, entry in enumerate(self._entries)}
        self._heapify()

    def insert(self, item, priority=None):
        """Insert method used to be able to insert new items with its priority"""
        # checks to see if the priority is None 
        if priority is None:
            priority = self._key(item)
    
        index = len(self._entries)

        # appends using Entry class
        self._entries.append(Entry(item, priority))
        # appends new entry to itemmap
        self._itemmap[item] = index

        # upheaps to keep heap balanced
        self._upheap(index)

    def _swap(self, a, b):
        """Swaps two elements of the priority queue"""
        L = self._entries
        va = L[a].item
        vb = L[b].item

        # updates the itemmap to reflect the swap
        self._itemmap[va] = b
        self._itemmap[vb] = a

        # swaps the entries
        L[a], L[b] = L[b], L[a]

    def changepriority(self, item, priority=None):
        """Changes the priority of an existing item in the Priority Queue"""
        if priority is None:
            priority = self._key(item)

        i = self._itemmap[item]

        # updates the priority of the entry
        self._entries[i].priority = priority

        # ensure that heap is balanced
        self._upheap(i)
        self._downheap(i)


    def removemin(self):
        """Removes and returns the item with the highest priority from the Priority Queue"""
        L = self._entries
        item = L[0].item

        # swaps the first and last elements
        self._swap(0, len(L) - 1)
        # removes the item from the itemmap
        del self._itemmap[item]
        # pops the last element
        L.pop()
        # downheaps to keep heap balanced
        self._downheap(0)

        return item
    
    def _heapify(self):
        """Builds the heap from the elements in the Priority Queue"""
        n = len(self._entries)

        # start from last non-leaf node - perform downheap to keep it balanced
        for i in reversed(range(n)):
            self._downheap(i)

    def __iter__(self):
        """Iterates over the Priority Queue"""
        return self
    
    def __next__(self):
        """Works alongside __iter__ to allow for iteration over the Priority Qieie"""
        if len(self) > 0:
            return self.removemin()
        else:
            raise StopIteration