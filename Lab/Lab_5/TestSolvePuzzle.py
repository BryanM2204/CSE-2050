from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                #tests to see if the puzzle function returns True when given a board that is solveable using only CW moves
                self.assertEqual(puzzle([3, 6, 4, 1, 3, 4, 2, 0]), True)
                self.assertEqual(puzzle([3, 6, 4, 1, 3, 4, 2, 0, 0]), True)

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                #tests to see if the puzzle function returns True when given a board that is solveable using only CCW moves
                self.assertTrue(puzzle([3, 2, 1, 2, 0]), True)
                self.assertTrue(puzzle([3, 2, 1, 2, 5, 8, 0]), True)


        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                #tests to see if the puzzle function returns True when given a board that is solveable using a combination of CW and CCW moves
                self.assertTrue(puzzle([3, 2, 1, 2, 1, 0]), True)
                self.assertTrue(puzzle([3, 2, 6, 3, 3, 1, 2, 1, 0]), True)
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                #tests to see if the puzzle function returns False when given a board that is unsolveable
                self.assertFalse(puzzle([3, 4, 1, 2, 0]), False)
                self.assertFalse(puzzle([3, 4, 1, 2, 3, 5, 0]), False)


unittest.main()