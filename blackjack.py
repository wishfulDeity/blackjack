import random


class Player:
    """Create a player with a hand.

    Args:
        name (str, default="Name"): The player's name.
    """

    def __init__(self, name="Name") -> None:
        self.name = name
        self.hand = []

    def hit(self, use_deck: list = [], amount: int = 1) -> None:
        """Does a hit (Draws card)

        Args:
            use_deck (list, default=[]): The deck being drawn from.
            amount (int, default=1): The amount of cards to draw.
        """
        for i in range(amount):
            drawn_card = random.choice(use_deck)
            drawn_card_index = use_deck.index(drawn_card)
            self.hand.append(use_deck.pop(drawn_card_index))

    # NOTE: I hate how this is implemented.
    def get_hand_value(self) -> None:
        """Gets the total value of the hand and puts it into
        self.hand_value.

        Also puts the player's status ("busted", "stand", "win", or "")
        """
        total_value = 0
        for card in self.hand:
            try:
                total_value += int(card)
            except ValueError:
                if card in ["j", "q", "k"]:
                    total_value += 10
                elif card == "a":
                    if total_value > 10:
                        total_value += 1
                    else:
                        total_value += 11

        self.hand_value = total_value

    def get_status(self):
        """Gets the player's status, if it's > 21, bust."""
        if self.hand_value > 21:
            self.status = "bust"
        elif self.hand_value == 21:
            self.status = "win"
        else:
            self.status = ""

    def stand(self):
        """Set self.status to "stand" """
        self.status = "stand"


class Dealer(Player):
    def __init__(self) -> None:
        pass

    def deal(self, deck, players=[Player]) -> None:
        for player in players:
            player.hit(deck, 2)


class CardDeck:
    """Create a card deck with `deck_count` packs in it

    Args:
        deck_count (int, default=1): The amount of packs to include in the deck
    """

    def __init__(self, deck_count=1) -> None:
        possible_cards = (
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
        )
        # Empty the deck
        new_deck = []

        # NOTE: Holy indentation.
        # Add a whole deck `deck_count` times
        for decks in range(deck_count):
            # Each deck has 4 suits
            for suit in range(4):
                # Add cards to the deck
                for card in range(len(possible_cards)):
                    new_deck.append(possible_cards[card])
        self.cards = new_deck


dealer = Dealer()
main_deck = CardDeck()


def main() -> None:
    print("Welcome to Blackjack!\n")
    player = Player(str(input("What is your name?: ")))
    player.get_hand_value()
    player.get_status()

    while player.status != "bust":
        player.get_hand_value()
        player.get_status()
        print(f"{player.name}'s hand:")
        for card in player.hand:
            print(card, end=" ")
        match str(input("(h)it or (s)tand?: ")).lower():
            case "h":
                player.hit(main_deck)
            case "s":
                player.stand()


if __name__ == "__main__":
    main()
