import random


class Player:
    def __init__(self, use_hand=[]) -> None:
        """_summary_ TODO

        Args:
            use_hand (list, default=[]): The list to use as the player's hand
        """
        self.hand = use_hand

    def hit(self, use_deck=[], amount=1):
        """Does a hit (Draws card)

        Args:
            use_deck (list): The deck being drawn from
            amount (int, default=1): The amount of cards to draw
        """
        for i in range(amount):
            drawn_card = random.choice(use_deck)
            drawn_card_index = use_deck.index(drawn_card)
            self.hand.append(drawn_card)
            use_deck.remove(drawn_card_index)

    def hand_value(self):
        total_hand = 0
        for card in self.hand:
            try:
                total_hand += int(card)
            except ValueError:
                if card in ["j", "q", "k"]:
                    total_hand += 10
                elif card == "a":  # TODO: Do this in literally any other way?
                    if total_hand > 10:
                        total_hand += 1
                    else:
                        total_hand += 11
        return total_hand


class DeckOfCards:
    def __init__(self, deck_count=1) -> None:
        """Create a card deck with `deck_count` packs in it

        Args:
            deck_count (int, default=1): The amount of packs to include in the deck
        """
        # Hardcoded cards because screw you that's why
        # Also a deck of cards GENERALLY doesn't change that much
        blackjack_cards = [
            "a",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "j",
            "q",
            "k",
        ]
        # Empty the deck
        new_deck = []

        # Add a whole deck `deck_count` times
        for decks in range(deck_count):
            for suit in range(4):  # Each deck has 4 suits
                for card in range(len(blackjack_cards)):  # Add cards to the deck
                    new_deck.append(blackjack_cards[card])

        self.cards = new_deck

    def __len__(self):
        return len(self.cards)


main_deck = DeckOfCards()

player1 = Player()
player1.hit(main_deck)


print(player1.hand_value())
print(main_deck.cards)
