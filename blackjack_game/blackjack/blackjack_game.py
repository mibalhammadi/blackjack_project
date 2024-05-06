from .deck import Deck

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.user_cards = []
        self.dealer_cards = []
        self.user_score = 0
        self.dealer_score = 0

    def deal_initial_cards(self):
        for i in range(2):  # Deal two cards each
            self.user_cards.append(self.deck.deal_card())
            self.dealer_cards.append(self.deck.deal_card())

    def calculate_score(self, cards):
        score = 0
        aces = 0
        for card, value in cards:
            if card.startswith('Ace'):
                aces += 1
            score += value
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def hit(self):
        card = self.deck.deal_card()
        self.user_cards.append(card)
        print(f"You received: {card[0]}")
        self.user_score = self.calculate_score(self.user_cards)
        print(f"Your Score: {self.user_score}")
        if self.user_score > 21:
            print("You Lost! Dealer wins.")
            return False
        return True

    def stand(self):
        self.dealer_score = self.calculate_score(self.dealer_cards)
        while self.dealer_score < 17:
            card = self.deck.deal_card()
            self.dealer_cards.append(card)
            self.dealer_score = self.calculate_score(self.dealer_cards)
        print(f"Dealer's Score: {self.dealer_score}")
        if self.dealer_score > 21 or self.user_score > self.dealer_score:
            print("You win!")
        else:
            print("Dealer wins.")

    def play_game(self):
        self.deal_initial_cards()
        self.user_score = self.calculate_score(self.user_cards)
        print(f"Your initial cards: {[card[0] for card in self.user_cards]}, Score: {self.user_score}")
        while True:
            action = input("Do you want to 'hit' or 'stand'? ")
            if action == 'h':
                if not self.hit():
                    break
            elif action == 's':
                self.stand()
                break
            else:
                print("Invalid action. Please type 'h' for hit or 's' for stand.")
