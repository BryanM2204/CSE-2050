import unittest
from BET import BETNode, create_trees, find_solutions, postfix_to_BET


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        r"""Tests evaluate method with calculated total - string representation of tree
               -
              / \
             *   5
            / \
           +   4
          / \
         2   3
        """

        # Test expression: 2 3 + 4 * 5 -
        postfix_expr = ['2', '3', '+', '4', '*', '5', '-']

        # implementation of method that takes a postfix expression and generates a BET from it
        # Stack ADT was used to do so - present in other file BET.py
        root = postfix_to_BET(postfix_expr)
        
        # correctly uses the evaluate method to find the value that the tree adds up to - in this case it is 15
        self.assertEqual(root.evaluate(), 15)


    def test_evaluate_tree2(self):
        r"""Tests evaluate method with calculated total - string representation of tree:
    
               +
              / \
             +   *
            / \   \
           2   3   5
                  /
                 4
        """
        # Test expression: 2 3 + 4 5 * +
        postfix_expr = ['2', '3', '+', '4', '5', '*', '+']

        # implementation of method that takes a postfix expression and generates a BET from it
        # Stack ADT was used to do so - present in other file BET.py
        root = postfix_to_BET(postfix_expr)

        # correctly uses the evaluate method to find the value that the tree adds up to - in this case it is 21
        self.assertEqual(root.evaluate(), 25)


class TestCreateTrees(unittest.TestCase):
    """Class tests the create_trees method"""
    def test_hand1(self):
        """Test a random hand in order to match with the number of possible trees - which is known to be 7680"""
        
        # choose 4 different cards
        cards = ['A', '2', '3', 'Q']
        
        # create trees
        trees = create_trees(cards)
        
        # assert that the length of trees is the same as the total possible number of trees
        self.assertEqual(len(trees), 7680)

        
    def test_hand2(self): 
        """Test a random hand in order to match with the number of possible trees - which is known to be 7680"""
        
        # choose 4 different cards
        cards = ['4', 'K', 'A', '5']

        # create trees
        trees = create_trees(cards)

        # assert that the length of trees is the same as the total possible number of trees
        self.assertEqual(len(trees), 7680)
        

class TestFindSolutions(unittest.TestCase):
    """Testing class that tests the find_solutions method"""
    def test0sols(self):
        """Tests for a hand that contains 0 solutions"""

        cards = ['K', 'K', 'K', 'K']

        # find_solutions is called - set of possible solutions is returned and assigned to solutions
        solutions = find_solutions(cards)

        # tests that the length of solutions is equal to 0
        self.assertEqual(len(solutions), 0)

    def test_A23Q(self):
        """Tests for a hand that contains 0 solutions"""

        cards = ['A', '2', '3', 'Q']

        # find_solutions is called - set of possible solutions is returned and assigned to solutions
        solutions = find_solutions(cards)

        # test that the length of possible solutions is equal to 33
        self.assertEqual(len(solutions), 33)
        
unittest.main()