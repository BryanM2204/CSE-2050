from hw3 import find_pairs_naive, find_pairs_optimized, measure_min_time
import unittest

class TestFindPairs(unittest.TestCase):
    def test_find_pairs_naive(self):
        """Tests the find_pairs_naive function"""

        # Tests the function with different lists and target numbers and edge cases
        self.assertSetEqual(find_pairs_naive([1, 2, 3, 4, 5, 6, 7], 8), {(1, 7), (3, 5), (6, 2)})
        self.assertSetEqual(find_pairs_naive([1, 2, 3, 4, 5, 6], 8), {(2, 6), (5, 3)})
        self.assertSetEqual(find_pairs_naive([1, 2, 3, 4, 5], 0), set())
        self.assertSetEqual(find_pairs_naive([1, 2, 3, 4, 5, 6], 12), set())
        self.assertSetEqual(find_pairs_naive([], 4), set())

    def test_find_pairs_optimized(self):
        """Tests the find_pairs_optimized function"""

        # Tests the optimized function with different lists and target numbers and edge cases
        self.assertSetEqual(find_pairs_optimized([1, 2, 3, 4, 5, 6, 7], 8), {(1, 7), (3, 5), (6, 2)})
        self.assertSetEqual(find_pairs_optimized([1, 2, 3, 4, 5, 6], 8), {(2, 6), (5, 3)})
        self.assertSetEqual(find_pairs_optimized([1, 2, 3, 4, 5], 0), set())
        self.assertSetEqual(find_pairs_optimized([1, 2, 3, 4, 5, 6], 12), set())
        self.assertSetEqual(find_pairs_optimized([], 5), set())

    def test_measure_min_time(self):
        """Tests the measure_min_time function"""

        # Tests the efficiency of the optimized function compared to the naive function
        self.assertLess(measure_min_time(find_pairs_optimized, ([i for i in range(1001)], 500)), measure_min_time(find_pairs_naive, ([i for i in range(1001)], 500)))


unittest.main()