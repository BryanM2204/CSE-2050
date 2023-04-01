class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Entry(key={self.key}, value={self.value})"
    
    def __eq__(self, other):
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)

class HashMapping:
    def __init__(self):
        self.m = 8                           # number of buckets
        self._len = 0
        self._L = [[] for i in range(self.m)] # list of buckets
        self.MINBUCKETS = 9

    def __len__(self):
        return self._len

    def __contains__(self, key):
        """Returns True (False) if key is (is not) in HashMapping"""
        # find the bucket
        idx = self._get_bkt_idx(key)

        # scan the bucket, return if you find it
        for entry in self._L[idx]:
            if entry.key == key:
                return True
            
        # return false
        return False

    def __setitem__(self, key, value):
        """Adds key:value pair to HashMapping, or updates hm[key] if it already exists"""
        idx = self._get_bkt_idx(key)
        for entry in self._L[idx]:
            if entry.key == key:
                entry.value = value
                return
        
        #if I didn't find the key
        self._L[idx].append(Entry(key, value))
        self._len += 1

        if len(self) > 2*self.m:
            self._rehash(2*self.m)
            

    def __getitem__(self, key):
        """Returns value associated with key. Raises KeyError if key not in HashMapping"""
        idx = self._get_bkt_idx(key)

        for entry in self._L[idx]:
            if entry.key == key:
                return entry.value
            
        raise KeyError(f'key {key} not found in HashMapping')

    def _get_bkt_idx(self, key):
        """Returns index of bucket key should be in"""
        return hash(key) % self.m
    
    def remove(self, key):
        """Remove key:value pair from hash mapping. Raise a KeyError if key not found"""
        # Maintain a lienar memory overhead (occasionally rehash down)
        idx = self._get_bkt_idx(key)

        #scan expected bucket for key
        for entry in self._L[idx]:

            # if key is found, remove, decrement lenght, rehash if appropriate
            if entry.key == key:
                self._L[idx].remove(entry)
                self._len -= 1
        
                if self.MINBUCKETS < len(self) < self.m/2:
                    self._rehash(self.m//2)

                return

        # key not found
        raise KeyError(f'key {key} not found in HashMapping')
    
    def _rehash(self, m_new):
        """Reahashes to m_new buckets"""
        # makea new list of buckets 
        new_L = [[] for i in range(m_new)]
        self.m = m_new

        # rehash every entry
        # look through every bucket
        for bucket in self._L:

            #look through every entry
            for entry in bucket:
                #rehash that entry
                idx = self._get_bkt_idx(entry.key)
                #add it to new_L
                new_L[idx].append(entry)

        # update self._L to new list
        self._L = new_L

if __name__ == '__main__':
    import random
    n = int(1E5)
    d = dict()
    hm = HashMapping()
    for i in range(n):
        new_k = random.randint(0, n)    # generate a random key

        if new_k not in d:              # check contains (false)
            assert new_k not in hm

        d[new_k] = str(new_k)           # add key to both collections
        hm[new_k] = str(new_k)

        assert new_k in hm              # check contains(True)
        assert hm[new_k] == d[new_k]    # getitem
        assert len(d) == len(hm)        # test len

    for i in range(n):
        if i in hm:
            hm.remove(i)
            assert not i in hm