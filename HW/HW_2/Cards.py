import random

class Deck:
    def __init__(self, values=[i for i in range(1, 14)], suits=['clubs', 'diamonds', 'hearts', 'spades'], card_list=[]):
        self.values = values
        self.suits = suits

        card_list = []
        for suit in self.suits:
            for value in self.values:
                card_list.append(Card(value, suit))

        self.card_list = card_list
    
    def __len__(self):
        return len(self.card_list)

    def sort(self):
        self.card_list.sort()
        return self.card_list

    def __repr__(self):
        return f'Deck: {self.card_list}'

    def shuffle(self):
        random.shuffle(self.card_list)
        return self.card_list

    def draw_top(self):
        top_card = self.card_list.pop(-1)
        if len(self.card_list) == 0:
            raise RuntimeError('Empty Deck')

        return f'{top_card}'

class Hand(Deck):

    def __init__(self, card_list):
        Deck.__init__(self)
        self.card_list = card_list

    def __repr__(self):
        return f'Hand: {self.card_list}'

    def play(self, card):

        if card not in self.card_list:
            raise RuntimeError('Card not in hand')

        self.card_list.remove(card)
        
        return card

class Card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f'Card({self.value} of {self.suit})'

    def __lt__(self, other):
        if self.suit[0] < other.suit[0]:
            return True
        
        elif self.suit[0] == other.suit[0]:
            if self.value < other.value:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.suit == other.suit and self.value == other.value:
            return True
        else:
            return False

