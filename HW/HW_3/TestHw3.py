from hw3 import find_pairs_naive
import unittest

class TestFindPairs(unittest.TestCase):
    def test_find_pairs_naive(self):
        self.assertEqual(find_pairs_naive([5, 7, 6, 1, 3, 2, 4, 8, 9], 10), {(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)})
        self.assertEqual(find_pairs_naive([6, 5, 2, 8, 9, 1], 7), {(1, 6), (2, 5), (8, 9)})
        self.assertEqual(find_pairs_naive([6, 5, 2, 8, 9, 1], 10), {(1, 9), (2, 8), (6, 5)})

# def test_find_pairs_optimized(self):


unittest.main()