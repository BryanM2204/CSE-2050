from math import floor, ceil, log2

class BSTNode:
    def __init__(self, key, value, left=None, right=None):
        """Creates a new BSTNode"""
        self.key = key
        self.value = value
        self.left = left
        self.right = right
       

    def put(self, key, value):
        """Adds key:value pair to BST, or updates value if key already in BST"""
        # 3 cases:

        # 1) we've found the key
        if key == self.key:
            self.value = value

        # 2) key < self.key
        if key < self.key:
            if self.left is None:
                self.left = BSTNode(key, value)
            # recursively search...
            else:
                self.left = self.left.put(key, value)

        # 3) key > self.key
        if key > self.key:
            if self.right is None:
                self.right = BSTNode(key, value)
            else:
                self.right = self.right.put(key, value)


        # once I implement alancing
        return self
    
        # any operation that can change the shape of my tree (put, remove) should
        # return the new root of this subtree when they finish
    
    def update_weight(self):
        """Updates weight of a node"""

        


    def get(self, key):
        """Returns value associated with key."""
        if key == self.key:
            return self.value
        if key < self.key:
            if self.left is None:
                raise KeyError(f"{key} not found")
            else:
                return self.left.get(key)
        if key > self.key:
            if self.right is None:
                raise KeyError(f"{key} not found")
            else:
                return self.right.get(key)
        

    def __contains__(self, key):
        """Returns True if key is in BST rooted at self"""
        # we've found the key
        if key == self.key:return True

        # key < self.key
        if key < self.key:
            if self.left is None: return False
            else:
                return self.left.get(key)
        
        # key > self.key
        if key > self.key:
            if self.right is None: return False
            else:
                return self.right.get(key)
        
        return False


    def __repr__(self):
        """Returns a string reprsentation of the BST"""
        L_strings = []
        self._repr(L_strings, level = 0)
       
        # L_strings is a list of lists, e.g.:
        # [['   ---4 ---   '],                          # tree level 0
        #  [' -2 - ', '  ', ' -6 - '],                  # tree level 1
        #  ['1 ', '  ', '3 ', '  ', '5 ', '  ', '7 ']]  # tree level 2


        L_joined = [''.join(level) for level in L_strings]  # join levels into 1 string each
        return '\n'.join(L_joined)                         # join all levels into 1 big string

    def _repr(self, L_strings, level):
        # add a new substring the first time we reach this level
        if level == len(L_strings):
            L_strings.append([])

            # check if we have previous aunts/uncles w/o children
            # manually add an offset on the left if we do.
            if level >= 1:
                offset = 0
                for item in L_strings[-2]:
                    offset+= len(item)
                L_strings[-1].append(' '*offset)
        
        
        # Fill in left tree
        if self.left:
            wa, wb = self.left._repr(L_strings, level+1)
        else:
            wa=wb=0

        # write this key, including left-buffer 
        key_width = max(len(str(self.key)), 3) # use at least 3 character long keys, so we get nic looking trees
        L_strings[level].append(' '*wa + '-'*wb + f"{self.key:^{key_width}}") 

        # insert spaces to all levels below, so newly added items have the correct left-offset
        for l in range(level+1, len(L_strings)): L_strings[l].append(' '*key_width)



        # fill in the right tree
        if self.right:
            wc, wd = self.right._repr(L_strings, level+1)
        else:
            wc=wd = 0

        # add right-buffer to this key
        L_strings[level][-1] += '-'*wc +' '*wd
        

        # return width of left and right trees
        return wa+wb+floor(key_width/2), wc+wd+ceil(key_width/2) 
            

        L_strings[level-1].append('-'*w_right)
if __name__ == '__main__':

    ### Some basic trees ###
    #    5
    #   4
    #  3
    # 2
    #1
    root = BSTNode(5, '5')
    for i in [4, 3, 2, 1]:
        root.put(i, str(i))
    print(root)
    print()


    # 9
    #  8
    #   7
    #    6
    #     5
    #      4
    #       3
    #        2
    #         1
    root = BSTNode(1, '1')
    for i in range(2, 10):
        root.put(i, str(i))
    print(root)
    print()


    #     4
    #  2       6
    # 1 3   5     7
    #          6.5
    root = BSTNode(4, '4')
    for i in [2, 6, 1, 3, 5, 7, 6.5]:
        assert not i in root
        root.put(i, str(i))
        assert i in root
    print(root)
    print()

    
    #     4
    #  2       6
    # 1 3   5     7
    #          6.5
    root = BSTNode('e', '4')
    for i in 'abcdfg':
        assert not i in root
        root.put(i, str(i))
        assert i in root
    print(root)
    print()
    ### Random tree ###
    import random
    newint = random.randint(0, 1000)
    #print(f"adding {newint}")
    root = BSTNode(newint, str(newint))
    for i in range(30):
        newint = random.randint(0, 1000)
        #print(f"adding {newint}")
        root.put(newint, str(newint))

    #import pdb; pdb.set_trace()
    print(root)