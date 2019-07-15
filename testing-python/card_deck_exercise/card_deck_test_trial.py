import unittest
from card_deck import Card, Deck


class TestingCardClass(unittest.TestCase):
    def setUp(self):
        """Set up the card object"""
        self.card = Card("A", "Hearts")

    def test_card_repr(self):
        """ Test the correct repr of the Card"""
        self.assertEqual(str(self.card), "A of Hearts")


class TestingDeckClass(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_repr(self):
        """Test that repr returns a deck of 52 cards when first initialized, no more no less"""
        self.assertEqual(str(self.deck), "Deck of 52 cards")


if __name__ == "__main__":
    unittest.main()
