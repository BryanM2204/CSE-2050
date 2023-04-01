class Entry:
    def __init__(self, key, value):
        "Initializes a new entry w/ key and value"
        self.key = key
        self.value = value

    def __repr__(self):
        "String representation of entry"
        return f"Entry(key={self.key}, value={self.value})"

class ListMapping():
    def __init__(self):
        "Add data structure to store entries"
        self._L = []
        
    def __setitem__(self, k, v):
        "Add key:value pair to Mapping, or updated value if key already in mapping"
        new_entry = Entry(k, v)
        for e in self._L:
            if e.key == k:
                e.value = v
                return
            
        self._L.append(new_entry)

    def __getitem__(self, k):
        "Return value associated with key. Raise a KeyError if key is not in mapping"
        for e in self._L:
            if e.key == k:
                return e.value
            
        raise KeyError(f"key {k} is not in ListMapping")
    


class HashMapping:
    def __init__(self):
        # create a list of empty "buckets"
        self.n_buckets = 8
        self._L = [[] for i in range(self.n_buckets)]
        self._len = 0

    def __len__(self):
        return self._len
    
    def find_bucket(self, key):
        return hash(key) % self.n_buckets
    
    def __setitem__(self, key, value):
        # 1) find which bucket key should be in 
        idx = self.find_bucket(key)
        # 2) scan that bucket - update value if you find key
        for e in self._L[idx]:
            if e.key == key:
                e.value = value
                return
                
        # 3) append new entry
        self._L[idx].append(Entry(key, value))

        self._len += 1

        # 4) If I have too many items: REHASH
        if len(self) > self.n_buckets:
            self.rehash(2*self.n_buckets)
    
    def rehash(self, n_buckets_new):
        # create a new list of buckets
        new_L = [[] for i in range(n_buckets_new)]

        # go trhough every exisiting entry and rehash
        for bucket in self._L:
            for entry in bucket:
                new_idx = self.find_bucket(entry.key)
                new_L[new_idx] = entry

        # redirect self._L to the new list
        self._L = new_L