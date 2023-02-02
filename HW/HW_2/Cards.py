import random

class Deck:
    'This class intializes a deck of cards and has methods that allow it to find the length, sort, print out the deck, shuffle, and draw a card'

    def __init__(self, values=[i for i in range(1, 14)], suits=['clubs', 'diamonds', 'hearts', 'spades'], card_list=[]):
        'initialize the deck with a list of values and suits'
        self.values = values
        self.suits = suits

        #create an empty list to hold the cards in the deck and then append each suit and value to the list
        card_list = []
        for suit in self.suits:
            for value in self.values:
                card_list.append(Card(value, suit))

        self.card_list = card_list
    
    def __len__(self):
        'method to find the length of the deck'
        return len(self.card_list)

    def sort(self):
        'method to sort the deck'
        self.card_list.sort()
        return self.card_list

    def __repr__(self):
        'method to print out the deck'
        return f'Deck: {self.card_list}'

    def shuffle(self):
        'method to shuffle the deck. Random is imported to shuffle the deck and is returned'
        random.shuffle(self.card_list)
        return self.card_list

    def draw_top(self):
        'method to draw the top card. The card is removed and then returned'

        #This checks to see if the deck is empty and it raises a RuntimeError if it is
        if len(self.card_list) == 0:
            raise RuntimeError('Empty Deck')
        
        #This removes the top card from the deck
        top_card = self.card_list.pop(-1)

        return f'{top_card}'

class Hand(Deck):
    'This class inherits from Deck class and has a play method that allows a card to be played'

    def __init__(self, card_list):
        'initialize the hand with a list of cards from the Deck class'
        Deck.__init__(self)
        self.card_list = card_list

    def __repr__(self):
        'method to print out the hand'
        return f'Hand: {self.card_list}'

    def play(self, card):
        'method to play a card. When the card is played, it is removed from the hand and returned'

        #Checks to see if the card is present in the hand and raises a RuntimeError if it isn't
        if card not in self.card_list:
            raise RuntimeError('Card not in hand')

        #Uses remove method to remove the specific card from the hand
        self.card_list.remove(card)
        
        return card

class Card:
    'this class initializes a card with a value and suit and is able to compare cards and checks if they are equal'

    def __init__(self, value, suit):
        'initializes a card with a value and suit'
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        'method to print out the card'
        return f'Card({self.value} of {self.suit})'

    def __lt__(self, other):
        'method to compare two cards. It checks if the first card is less than the second card based on suit and value'

        #Uses index to compare the first letter of the suit to determine which suit is greater
        if self.suit[0] < other.suit[0]:
            return True
        
        #If the suits are equal, it then compares the values and  returns true of self.value is lesser than other.value
        #If the suits are not equal, it returns false
        elif self.suit[0] == other.suit[0]:
            if self.value < other.value:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        'method to check if two cards are equal. Checks both suit and value'

        #Uses if statement to check for suit and value, and returns true if they are indeed equal
        if self.suit == other.suit and self.value == other.value:
            return True
        else:
            return False

