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
        self._cards = []


card = Card('Hearts', "A")

print(card)


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
mytest = [[comb2, [comb for comb in suits]] for comb2 in values]
print(mytest)
