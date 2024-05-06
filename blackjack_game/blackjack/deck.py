import random

class Deck:
    def __init__(self):
        """Initialize the deck of cards."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
                 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.deck = []
        for suit in suits:
            for rank, value in ranks.items():
                card = f"{rank} of {suit}"
                self.deck.append((card, value))

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)

    def deal_card(self):
        """Deal a single card from the deck."""
        return self.deck.pop()