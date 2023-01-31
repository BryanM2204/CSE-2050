from Cards import Card, Deck
import unittest

class TestCard(unittest.TestCase):
    "Test cases specific to the Card class"
    def setUp(self):
        self.c1 = Card(9, 'spades')
        self.c2 = Card(1, 'hearts')
        self.c3 = Card(5, 'diamonds')
        self.c4 = Card(8, 'clubs')
        self.c5 = Card(9, 'spades')

    def test_init(self):
        self.assertEqual(self.c1.value, 9)
        self.assertEqual(self.c1.suit, 'spades')

        self.assertEqual(self.c2.value, 1)
        self.assertEqual(self.c2.suit, 'hearts')

        self.assertEqual(self.c3.value, 5)
        self.assertEqual(self.c3.suit, 'diamonds')

    def test_repr(self):
        self.assertEqual(repr(self.c1), 'Card(9 of spades)')
        self.assertEqual(repr(self.c2), 'Card(1 of hearts)')
        self.assertEqual(repr(self.c3), 'Card(5 of diamonds)')

    def test_lt(self):
        self.assertTrue(self.c4 < self.c1)
        self.assertFalse(self.c2 < self.c3)
        self.assertTrue(self.c2 < self.c1)

    def test_eq(self):
        self.assertEqual(self.c1, self.c5)
        self.assertNotEqual(self.c1, self.c2)

class TestDeck(unittest.TestCase):
    "Test cases specific to the Deck class"

    def setUp(self):
        self.d1 = Deck()
        self.d2 = Deck([1, 2, 3], ['Dog', 'Cat', 'Bird'])
        self.d3 = Deck([1, 2], ['Blue', 'Red'])

    def test_init(self):
        self.assertEqual(self.d1.values, [i for i in range(1, 14)])
        self.assertEqual(self.d1.suits, ['clubs', 'diamonds', 'hearts', 'spades'])

        self.assertEqual(self.d2.values, [1, 2, 3])
        self.assertEqual(self.d2.suits, ['Dog', 'Cat', 'Bird'])

        self.assertEqual(self.d3.values, [1, 2])
        self.assertEqual(self.d3.suits, ['Blue', 'Red'])

    def test_len(self):
        self.assertEqual(len(self.d1), 52)
        self.assertEqual(len(self.d2), 9)
        self.assertEqual(len(self.d3), 4)

    def test_sort(self):
        self.assertNotEquals(self.d1.card_list, self.d1.card_list.sort())
        self.assertNotEquals(self.d2.card_list, self.d2.card_list.sort())
        self.assertNotEquals(self.d3.card_list, self.d3.card_list.sort())

    def test_repr(self):
        self.assertEqual(repr(self.d3), 'Deck: [Card(1 of Blue), Card(2 of Blue), Card(1 of Red), Card(2 of Red)]') 

    def test_shuffle(self):
        self.assertNotEquals(self.d1.card_list, self.d1.shuffle())


# class TestHand(unittest.TestCase):
#     "Test cases specific to the Hand class"

#     def test_init(self):

unittest.main()