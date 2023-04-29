import itertools

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, value): 
        """Add a new node to the left of this node"""

        # assigns node to self.left if self.left was previously None - else: keep recursively going left
        if self.left is None: self.left = BETNode(value)
        else: self.left.add_left(value)

        return self
    
    def add_right(self, value): 
        """Add a new node to the right of this node"""

        # assigns node to self.right if self.right was previously None - else: keep recursively going right
        if self.right is None: self.right = BETNode(value)
        else: self.right.add_right(value)

        return self

    def evaluate(self):
        """Evaluate the expression tree"""
        # base case - if element is a card value, then simply return value
        if self.value in BETNode.CARD_VAL_DICT: return BETNode.CARD_VAL_DICT[self.value]

        # if element is an operator, then evaluate the left and right subtrees
        if self.value in BETNode.OPERATORS:
            left = self.left.evaluate()
            right = self.right.evaluate()

            # if right or left are none - returns none
            if left is None or right is None: return None

            # if operator is +, then return sum of left and right subtrees
            if self.value == '+': return left + right

            # if operator is -, then return difference of left and right subtrees
            if self.value == '-': return left - right

            # if operator is *, then return product of left and right subtrees
            if self.value == '*': return left * right

            # if operator is /, then return quotient of left and right subtrees - may end up dividing by 0, so return None
            if self.value == '/': 
                if right == 0: return None
                else: return left / right


    def __repr__(self):
        """Returns a string representation of the BET"""
        # base case -- if element is a card value, then simply return value
        if self.left is None and self.right is None:
            return str(self.value)
        
        # recursively call repr - assings with returned value
        left_str = repr(self.left)
        right_str = repr(self.right)

        # returns a string with the correct operations and cards
        return f'({left_str}{self.value}{right_str})'


def create_trees(cards):
    """Create all possible binary expression trees for the given cards"""
    # base case - if there is only one card, then return a list containing a tree with that card as the root
    if len(cards) == 1: return [BETNode(cards[0])]

    # create an empty list to store all possible trees
    trees = set()

    # iterate through all possible combinations of card using intertools
    for i in range(1, len(cards)):
        for left_cards in itertools.combinations(cards, i):
            right_cards = tuple(c for c in cards if c not in left_cards)

            # create a list of all possible trees for the left and right subtrees
            left_trees = create_trees(left_cards)
            right_trees = create_trees(right_cards)

            # iterate through all possible operators
            for operator in BETNode.OPERATORS:
                # iterate through all possible combinations of left and right trees
                for left_tree, right_tree in itertools.product(left_trees, right_trees):
                    # create a new tree with the operator as the root and left and right subtrees
                    tree = BETNode(operator, left_tree, right_tree)

                    # add the tree to the list of all possible trees
                    trees.add(tree)

    return trees

def find_solutions(cards):
    """Find all possible solutions for the given cards"""
    # create a set to store all possible solutions
    solutions = set()

    # create a list of all possible trees
    trees = create_trees(cards)

    # evaluate each tree and finds all ways to get 24 - stores string representation of each card in set using repr
    for tree in trees:
        if tree.evaluate() == 24: solutions.add(repr(tree))

    return solutions

def postfix_to_BET(postfix):
    """
    Takes a postfix expression and generates a BET from it.

    param postfix: a postfix expression
    returns a BETNode representing the expression

    implementation of a stack ADT - make testing more easier when creating BET
    """

    stack = []

    # for loop that iterates through the parameter which is a list of cards and operations representing what will be in the tree
    for token in postfix:
        # if token is an operator, then pop the last two elements from the stack and create a new node with the operator as the root and the last two elements as the left and right subtree
        if token in BETNode.OPERATORS:
            right = stack.pop()
            left = stack.pop()
            # appends to stack list with the appropriate orientation of the operator and left and right cards
            stack.append(BETNode(token, left, right))
        else:
            # appends if the token is not an operator 
            stack.append(BETNode(token))

    # returns the stack list with pop()
    return stack.pop()

