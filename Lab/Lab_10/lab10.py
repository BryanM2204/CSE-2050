# This file empty on purpose - add the correct classes/methods below
class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        return self.item == other.item and self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"Entry(item={self.item}, priority={self.priority})"
    
class PQ_UL:
    def __init__(self):
        self._L = []
    
    def __len__(self):
        return len(self._L)
    
    def insert(self, item, priority):
        new_entry = Entry(item=item, priority=priority)

        self._L.append(new_entry)


    def find_min(self):
        # item with minimum priority
        min_entry = self._L[0]
        
        for entry in self._L:
            if entry < min_entry:
                min_entry = entry

        return min_entry


    def remove_min(self):
        # remove and return item with minimum priority
        min_entry = self.find_min()
        self._L.remove(min_entry)
        return min_entry

class PQ_OL:

    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)

    def insert(self, item, priority):
        new_entry = Entry(item=item, priority=priority)

        self._L.append(new_entry)

    def find_min(self):
        # item with minimum priority
        min_entry = self._L[0]
        
        for entry in self._L:
            if entry < min_entry:
                min_entry = entry

        return min_entry

    def remove_min(self):
        # remove and return item with minimum priority
        min_entry = self.find_min()
        self._L.remove(min_entry)
        return min_entry
    

