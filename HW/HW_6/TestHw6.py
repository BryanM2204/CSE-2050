import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted

# TODO: implement tests for sort_halfsorted

class Test_SortHalfSorted(unittest.TestCase):
   def test_halfsorted_bubble(self):
      'test bubble sort on a half-sorted list'
      # use sort_halfsorted(L, bubble) to test

      # tests a range of lengths and pattersn from 1 to 50 
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        # generates a halfsorted list using n for each pattern
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        # create a deep copy of list using splicing
                        deep_copy = L[:]
                        # sorts the original list
                        sort_halfsorted(L, bubble)
                        # test that the original list is now sorted
                        self.assertTrue(is_sorted(L))
                        # test that the orignal list and the deep copy have the same elements
                        self.assertCountEqual(L, deep_copy)
                        
   def test_halfosrted_selection(self):
      'test a selection sort on half-sorted lists'
      # use sort_halfsorted(L, selection) to test

      # tests a range of lengths and pattersn from 1 to 50
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        # generates a halfsorted list using n for each pattern
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        # create a deep copy of list using splicing
                        deep_copy = L[:]
                        # sorts the original list
                        sort_halfsorted(L, selection)
                        # test that the original list is now sorted
                        self.assertTrue(is_sorted(L))
                        # test that the orignal list and the deep copy have the same elements
                        self.assertCountEqual(L, deep_copy)

   def test_halfsorted_insertion(self): 
      'test an insertion sort on half-sorted lists'
      # use sort_halfsorted(L, insertion) to test
      
      # test a range of lengths and patterns from 1 - 50
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        # generates a halfsorted list using n for each pattern
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        # create a deep copy of list using splicing
                        deep_copy = L[:]
                        # sorts the original list
                        sort_halfsorted(L, insertion)
                        # test that the original list is now sorted
                        self.assertTrue(is_sorted(L))
                        # test that the orignal list and the deep copy have the same elements
                        self.assertCountEqual(L, deep_copy)

# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()

