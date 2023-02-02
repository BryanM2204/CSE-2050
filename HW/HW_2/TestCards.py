from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase):
    "Test cases specific to the Card class"
    def setUp(self):
        'Sets up the card class for testing'
        self.c1 = Card(9, 'spades')
        self.c2 = Card(1, 'hearts')
        self.c3 = Card(5, 'diamonds')
        self.c4 = Card(8, 'clubs')
        self.c5 = Card(9, 'spades')

    def test_init(self):
        'Tests the initialization of the card class'

        #This checks to see if the value and suit are both initialized correctly
        self.assertEqual(self.c1.value, 9)
        self.assertEqual(self.c1.suit, 'spades')

        self.assertEqual(self.c2.value, 1)
        self.assertEqual(self.c2.suit, 'hearts')

        self.assertEqual(self.c3.value, 5)
        self.assertEqual(self.c3.suit, 'diamonds')

    def test_repr(self):
        'Tests the repr method of the card class'

        #Checks to see if the repr method matches the expected string
        self.assertEqual(repr(self.c1), 'Card(9 of spades)')
        self.assertEqual(repr(self.c2), 'Card(1 of hearts)')
        self.assertEqual(repr(self.c3), 'Card(5 of diamonds)')

    def test_lt(self):
        'Tests the lt method of the card class'
       
        #Compares two cards and uses an assert test to see if the expected result is true or false
        self.assertTrue(self.c4 < self.c1)
        self.assertFalse(self.c2 < self.c3)
        self.assertTrue(self.c2 < self.c1)

    def test_eq(self):
        'Tests the eq method of the card class'

        #Compares two cards and uses an assert test to see if the expected result is true or false
        self.assertEqual(self.c1, self.c5)
        self.assertNotEqual(self.c1, self.c2)

class TestDeck(unittest.TestCase):
    "Test cases specific to the Deck class"

    def setUp(self):
        'Sets up the deck class for testing'
        self.d1 = Deck()
        self.d2 = Deck([1, 2, 3], ['Dog', 'Cat', 'Bird'])
        self.d3 = Deck([1, 2], ['Blue', 'Red'])

    def test_init(self):
        'Tests the initialization of the deck class'

        #Checks to see if the values and suits are initialized correctly
        self.assertEqual(self.d1.values, [i for i in range(1, 14)])
        self.assertEqual(self.d1.suits, ['clubs', 'diamonds', 'hearts', 'spades'])

        self.assertEqual(self.d2.values, [1, 2, 3])
        self.assertEqual(self.d2.suits, ['Dog', 'Cat', 'Bird'])

        self.assertEqual(self.d3.values, [1, 2])
        self.assertEqual(self.d3.suits, ['Blue', 'Red'])

    def test_len(self):
        'Tests the len method of the deck class'

        #Checks to see if the length of each deck matches with the correct number
        self.assertEqual(len(self.d1), 52)
        self.assertEqual(len(self.d2), 9)
        self.assertEqual(len(self.d3), 4)

    def test_sort(self):
        'Tests the sort method of the deck class'

        #Uses the sort method to sort the deck and then compares the sorted deck to the original deck
        self.assertNotEquals(self.d1.card_list, self.d1.card_list.sort())
        self.assertNotEquals(self.d2.card_list, self.d2.card_list.sort())
        self.assertNotEquals(self.d3.card_list, self.d3.card_list.sort())

    def test_repr(self):
        'Tests the repr method of the deck class'

        #Checks to see if the repr method matches the expected string
        self.assertEqual(repr(self.d3), 'Deck: [Card(1 of Blue), Card(2 of Blue), Card(1 of Red), Card(2 of Red)]') 

    def test_shuffle(self):
        'Tests the shuffle method of the deck class'

        #Uses the shuffle method to shuffle the deck and then compares it to the original deck to see if they are different
        self.assertNotEquals(self.d1.card_list[:], self.d1.shuffle())
        self.assertNotEquals(self.d2.card_list[:], self.d2.shuffle())
        self.assertNotEquals(self.d3.card_list[:], self.d3.shuffle())
    
    def test_draw_top(self):
        'Tests the draw_top method of the deck class'

        #Uses the draw_top method to draw the top card of the deck and then compares it to the expected string
        self.assertEqual(self.d1.draw_top(), 'Card(13 of spades)')
        self.assertEqual(self.d2.draw_top(), 'Card(3 of Bird)')
        self.assertEqual(self.d3.draw_top(), 'Card(2 of Red)')

class TestHand(unittest.TestCase):
    "Test cases specific to the Hand class"

    def setUp(self):
        'Sets up the hand class for testing'

        #Creates hands with different cards
        self.h1 = Hand([Card(value, 'spades') for value in range (5, 0, -1)])
        self.h2 = Hand([Card(value, 'hearts') for value in range (5, 0, -1)])
        self.h3 = Hand([Card(value, 'diamonds') for value in range (5, 0, -1)])

    def test_init(self):
        'Tests the initialization of the hand class'

        #Checks to see if the cards are initialized correctly by comparing the card list to the expected list
        self.assertEqual(self.h1.card_list, [Card(value, 'spades') for value in range (5, 0, -1)])
        self.assertEqual(self.h2.card_list, [Card(value, 'hearts') for value in range (5, 0, -1)])
        self.assertEqual(self.h3.card_list, [Card(value, 'diamonds') for value in range (5, 0, -1)])

    def test_repr(self):
        'Tests the repr method of the hand class'

        #Uses the repr method to compare the string to the expected string
        self.assertEqual(repr(self.h1), 'Hand: [Card(5 of spades), Card(4 of spades), Card(3 of spades), Card(2 of spades), Card(1 of spades)]')
        self.assertEqual(repr(self.h2), 'Hand: [Card(5 of hearts), Card(4 of hearts), Card(3 of hearts), Card(2 of hearts), Card(1 of hearts)]')
        self.assertEqual(repr(self.h3), 'Hand: [Card(5 of diamonds), Card(4 of diamonds), Card(3 of diamonds), Card(2 of diamonds), Card(1 of diamonds)]')

    def test_play(self):
        'Tests the play method of the hand class'

        #Uses the play method to play a card and then compares it to the expected card
        self.assertEquals(self.h1.play(Card(1, 'spades')), Card(1, 'spades'))
        self.assertEquals(self.h2.play(Card(1, 'hearts')), Card(1, 'hearts'))
        self.assertEquals(self.h3.play(Card(1, 'diamonds')), Card(1, 'diamonds'))



unittest.main()