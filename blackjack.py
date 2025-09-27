import random
import time
import sys

# Huge Shoutout to https://stackoverflow.com/questions/69946172/how-can-i-print-my-ascii-cards-side-by-side
# They provided the code for the card art

# Duh, this is just all the dependencies. Sys is only really here for fun.


"""Classes and their methods"""

# Actually creates the cards to be used in deck. Most of these are basically "blank objects"
class Card:
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

# Changes how the strings are read off. Users will always see x of y
    def __repr__(self):
        return self._value + " of " + self._suit


# Evil line of code to make sure each card has a proper value. (JQK: 10 | A: 1, 11)
    def blackjack_values(self):
        if self._value in ["Jack", "Queen", "King"]:
            return 10
        elif self._value == "Ace":
            return (1, 11)
        else:
            return int(self._value)



# Defines the deck, card values, shuffling the deck, and dealing
class Deck:
    def __init__(self):
        value = [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]
        suit = [ "Clubs", "Diamonds", "Hearts", "Spades" ]
        self.cards = [Card(v, s) for s in suit for v in value]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num=2):
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt_cards


# Time to make a person. Oh brother

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.standing = False
        self.score = 0

    def get_cards(self, cards):
        self.hand.extend(cards)

    def hand_value(self):
        return valid_dealt(self.hand)

    def view_hand(self):
        return self.hand

    def player_hit(self, deck):
        new = deck.deal(1)
        self.get_cards(new)
        print(f"{self.name} hits.")

    def player_stand(self):
        self.standing = True
        print(f"{self.name} taps out.")

# Time to make a second person. Luckily, I already have one!

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

        # Since I made 21 an integer (in the event there were multiple numbers but one was 21), I need this stand flag
        # Earlier was just list checking, so it might hit on 21 (off draw)
        # Admittedly this is longer than it could be, but it helps for my vision

    def should_hit(self):
        hand = valid_dealt(self.hand)
        if isinstance(hand, list):
            if not hand:
                return False
            maxv = max(hand)
            if maxv < 17:
                return True
            else:
                return False
        else:
            return False

        # Likely there won't be an index error.
        # But if something is truly cooked later, might as well handle it here

    def show_one(self):
        if self.hand:
            return self.hand[0]
        else:
            return None



"""Functions and their stuff"""

# Make sure the deck is real. I'm 90% sure this is useless, but its fun to have
def integriddy(deck):
    if len(deck.cards) == 52:
        print("Dealer shuffles the hand...")
    else:
        print("Dealer is missing cards. Something went terribly wrong.")
        time.sleep(1)
        sys.exit()


# Actually define a value for the hand. Helpful for the user, and can list multiple when an Ace is dealt.
def handvalue(cards):
    totals = [0]

    for card in cards:
        vals = card.blackjack_values()
        if isinstance(vals, tuple):
            temp_total = []
            for total in totals:
                for val in vals:
                    temp_total.append(total + val)
            totals = temp_total
        else:
            totals = [total + vals for total in totals]
    cleaning = sorted(set(totals))
    return cleaning


# Makes sure the user only sees the valid hands. If an Ace combo goes over 21, show the lowest.
def valid_dealt(cards):
    totals = handvalue(cards)
    valid_totals = [total for total in totals if total <=21]

    if 21 in valid_totals:
        return 21
    else:
        return valid_totals

def mk_card(s):
    pcarddisplay = [] 
    pcarddisplay.append("┌─────────┐")
    # We'll fill rank left on line 1 and right on line 7 with spaces, no dots
    pcarddisplay.append("│{}        │")  # placeholder for top rank
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . {} . .│")  # suit symbol centered here
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│        {}│")  # placeholder for bottom rank
    pcarddisplay.append("└─────────┘")

    rank = s.split()[0]  # Get rank part (e.g., "10", "King", "2")

    # Convert face cards to single letter symbol
    if rank == "10":
        rank_top = rank_bottom = "10"
    elif rank in ["Jack", "Queen", "King", "Ace"]:
        rank_top = rank_bottom = rank[0]  # J, Q, K, A
    else:
        rank_top = rank_bottom = rank  # Numbers like 2-9

    # Fill line 1 with rank left aligned
    if len(rank_top) == 2:
        pcarddisplay[1] = f"│{rank_top}       │"  # 2 chars + 7 spaces
    else:
        pcarddisplay[1] = f"│{rank_top}        │"  # 1 char + 8 spaces

    # Fill line 7 with rank right aligned
    if len(rank_bottom) == 2:
        pcarddisplay[7] = f"│       {rank_bottom}│"  # 7 spaces + 2 chars
    else:
        pcarddisplay[7] = f"│        {rank_bottom}│"  # 8 spaces + 1 char

    # Put the suit symbol in the middle line (index 4)
    if "Diamonds" in s:
        pcarddisplay[4] = "│. . ♦ . .│"
    elif "Clubs" in s:
        pcarddisplay[4] = "│. . ♣ . .│"
    elif "Hearts" in s:
        pcarddisplay[4] = "│. . ♥ . .│"
    elif "Spades" in s:
        pcarddisplay[4] = "│. . ♠ . .│"

    return pcarddisplay




def print_hand(cards, who="Player"):
    hand_strs = [str(card) for card in cards]
    card_lines = list(zip(*(mk_card(c) for c in hand_strs)))

    print(f"{who}'s hand:")
    for line_group in card_lines:
        print('  '.join(line_group))
    print()

def game_turn(deck, player, dealer):

    hand = player.hand_value()
    print()
    print_hand(player.hand, player.name)
    print(f"Hand Value: {player.hand_value()}")
    print()

    print(f"Dealer turns over one card: {dealer.show_one()}")
    print()

    while True:
        hand = player.hand_value()
        if hand == 21:
            print("Hand is worth 21")
            break

        if isinstance(hand, list) and not hand:
            print(f"{player.name} has busted.")
            print()
            break

        while True:
            player_act = input("Would you like to hit or stand? (hint: type h/s) ").lower()
            if player_act not in ("h", "s"):
                continue
            else:
                break

        if player_act == "h":
            print()
            player.player_hit(deck)
            time.sleep(1)
            print()
            print_hand(player.hand, player.name)
            print(f"Hand Value: {player.hand_value()}")
            print()

        else:
            player.player_stand()
            break

    print("Dealer to play...")
    dealer_hand = dealer.hand_value()
    time.sleep(1)

    while dealer.should_hit():
        time.sleep(1)
        print()
        dealer.player_hit(deck)
        time.sleep(2)
        print()
        print_hand(dealer.hand, "Dealer")
        dealer_hand = dealer.hand_value()
        print(f"Hand Value: {dealer_hand}")
        print()

    if isinstance(dealer_hand, list) and not dealer_hand:
        print(f"Dealer has busted.")
        print()
    else:
        print(f"Dealer stands on hand {dealer_hand}")
        time.sleep(1)

def game_winner(player, dealer):
    player_hand = player.hand_value()
    dealer_hand = dealer.hand_value()

    def best(hand):
        if isinstance(hand, int):
            return int(hand)
        elif isinstance(hand, list) and hand:
            return int(max(hand))
        else:
            return None

    finalhandp = best(player_hand)
    finalhandd = best(dealer_hand)


    print("Final hands...")
    print()
    time.sleep(2)
    print(f"{player.name} has {player.view_hand()} valued at {finalhandp if finalhandp else 'Bust!'}")
    print(f"Dealer has {dealer.view_hand()} valued at {finalhandd if finalhandd else 'Bust!'}")
    print()

    if finalhandp is None and finalhandd is None:
        print("There is a tie. Table has pushed!")
    else:
        if finalhandp is None and finalhandd:
            print("Dealer Wins!")
            dealer.score += 1
        elif finalhandd is None and finalhandp:
            print("Player Wins!")
            player.score += 1
        elif finalhandp > finalhandd:
            print(f"Player Wins! {finalhandp} > {finalhandd}")
            player.score += 1
        elif finalhandd > finalhandp:
            print(f"Dealer Wins! {finalhandd} > {finalhandp}")
            dealer.score += 1
        else:
            print("There is a tie. Table has pushed!")



""" Actual Lines of Stuff"""

def main():
    print("Welcome to blackjack! Tell us your name and you'll be dealt in.")
    name = input("").capitalize()
    player = Player(name)
    dealer = Dealer()

    while True:
        #Game Setup and Check
        deck = Deck()
        deck.shuffle()
        integriddy(deck)
        
        player.hand.clear()
        player.standing = False
        dealer.hand.clear()
        dealer.standing = False

        for _ in range(2):
            player.get_cards(deck.deal(1))
            dealer.get_cards(deck.deal(1))

        game_turn(deck, player, dealer)
        game_winner(player, dealer)
        print()
        print(f"Current Scores: {player.name}: {player.score} | Dealer: {dealer.score}")
        print()


        key = input("Press enter to play again! Type 'Stop' to quit.  ").lower().strip()
        if key == "stop":
            #print(earnings?)
            print("Have a nice day!")
            break

        print()
    


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)
