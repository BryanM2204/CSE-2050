import unittest
import random
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


class Test_linear_scan(unittest.TestCase): 
    def test_linear_scan(self):
        "tests the linear_scan method"
        # Edge case - list is already sorted
        L = [1, 2, 3, 4, 5]
        self.assertEqual(linear_scan(L), "sorted") 

        # Edge case - list is sorted in reverse
        L1 = [5, 4, 3, 2, 1]
        L2 = [100, 50, 30, 20, 10, 1]
        self.assertEqual(linear_scan(L1), "reverse-list") 
        self.assertEqual(linear_scan(L2), "reverse-list")

        # Edge case - there are at most 5 items out of place
        L = [13, 1, 20, 2, 5, 3, 10, 6]
        self.assertEqual(linear_scan(L), "insertion")

        # Edge case - there are more than 5 items out of place
        L = [100, 13, 1, 20, 2, 5, 3, 10, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, -1, 0]
        self.assertEqual(linear_scan(L), None)

class Test_reverse_list(unittest.TestCase): 
    def test_reverse_list(self): 
        "tests the reverse_list method"
        L = [100, 50, 20, 10, 5, 3, 2, 1]
        # tests that the list is now in increasing order
        self.assertEqual(reverse_list(L), [1, 2, 3, 5, 10, 20, 50, 100])
        

class Test_insertionsort(unittest.TestCase): 
    def test_insertionsort(self):
        "tests the insertionsort method"
        n = int(100) 
        #creates a list of 100 numbers
        L = [(n-i) for i in range(n)]
        #shuffles the list
        random.shuffle(L)
        insertionsort(L)
        # tests to see that the list is sorted
        self.assertEqual(L, [i+1 for i in range(n)])

class Test_quicksort(unittest.TestCase): 
    def test_quicksort(self):
        "tests the quicksort method"
        n = int(100) 
        #creates a list of 100 numbers
        L = [(n-i) for i in range(n)]
        #shuffles the list
        random.shuffle(L)
        quicksort(L)
        # tests to see that the list is sorted
        self.assertEqual(L, [i+1 for i in range(n)])

class Test_mergesort(unittest.TestCase): 
    def test_mergesort(self):
        "tests the mergesort method"
        n = int(100) 
        #creates a list of 100 numbers
        L = [(n-i) for i in range(n)]
        #shuffles the list
        random.shuffle(L)
        mergesort(L)
        # tests that the list is sorted
        self.assertEqual(L, [i+1 for i in range(n)])

class Test_magicsort(unittest.TestCase): 
    def test_magicsort(self):
        "tests the magicsort method"
        n = int(1E5) 
        #creates a list of 1E5 numbers in reverse order
        L1 = [(n-i) for i in range(n)]
        # tests that the list is reversed and is outputted by magic_sort
        self.assertEqual(magic_sort(L1), {'reverse-list'})

        L2 = [(n-i) for i in range(n)]
        # appends the list of numbers in reverse with 8 negative numbers at the beginning
        L2[:6] = [-1, -2, -3, -4, -5, -6, -7, -8]
        # tests that magic_sort outputs quicksort, mergesort, and insertionsort
        self.assertEqual(magic_sort(L2), {'quicksort', 'mergesort', 'insertionsort'})

unittest.main()