import random


class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def __repr__(self):
        return f'{self._value} of {self._suit} '


class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self._cards = [Deck(suit, value)
                       for suit in Deck.suits for value in Deck.values]

    def count(self):
        return len(self._cards)

    def __repr__(self):
        card_count = self.count()
        return f'Deck of {card_count} cards'

    def _deal(self, number):
        card_count = self.count()
        if card_count == 0:
            raise ValueError('All cards have been dealt')
        if card_count < number:
            all_cards = self._cards.copy()
            self._cards.clear()
            return all_cards
        else:
            if number == 1:
                return self._cards.pop(random.randint(0, card_count-1))
            else:
                dealt_cards = list()
                for i in range(number):
                    card_count = self.count()
                    dealt_cards.append(self._cards.pop(
                        random.randint(0, card_count-1)))
                return dealt_cards

    def shuffle(self):
        card_count = self.count()
        if card_count < 52:
            raise ValueError('Only Full decks can be shuffled')
        random.shuffle(self._cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, number):
        return self._deal(number)

    def all_cards(self):
        return self._cards


testDeck = Deck()
# print(testDeck.all_cards())
testDeck.shuffle()
# print(testDeck.all_cards())
print(testDeck.count())
print(testDeck.deal_card())
print(testDeck.count())
print(testDeck.deal_hand(53))
print(testDeck.count())
# print(testDeck.deal_card())
print(testDeck)
# testDeck.shuffle()
