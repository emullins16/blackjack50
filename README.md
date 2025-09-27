 # Python Blackjack
    #### Video Demo: https://youtu.be/Ptq0IcX2l5w
    #### Description:

    For my CS50P final project, I recreated one of the most commonly played casino games, 21 (or Blackjack), where player races the house to reach a hand valuing 21 while not going over.
    While the game mimic the gameplay of the traditional card game, the ability to bet money (even fake), has not been implemented as to discourage gambling.

    For the gameplay loop, the player is dealt a hand of two cards while being able to see one of two dealer cards.
    At this point, they are prompted with the option to hit or stand. If they hit, they will be dealt another card, and if they stand, the dealer will play.
    The classic dealer rules have been implemented such that they will hit until they reach a hand value of at least 17, at which point they will stand.

    Once both players have been dealt their hands, the house runs code to figure out which hand has been dealt a higher value, at which point it will award a point to the winning user.
    Because a push essentially results in both sides gaining one point, no points are awarded for pushing.

    At the end of the game, the user can choose to play again OR to exit via typing "stop"

 ## Main Code Breakdown

   There are four total classes in this project.
   - "Deck" which contains 52 cards. Thirteen values divided into four suits with no repeats. The deck is fully shufflable, and card dealing is handled in this class
   - "Card" which processes the values assigned to each card into a deck and outputs them into readable code. Basically, it takes the objects from Deck and turns them into something usable.
   - "Player" is an overall class that is able to recieve cards, view cards, hit to be dealt more cards, and stand to "end their turn". The score for each player is also held here instead of in main.
   - "Dealer" is a class that inherits the logic of player, but extends it with extra code to implement teh dealer logic.

   There are also five total secondary functions in this project.
   - "integriddy" A coding artifact from testing the validity of the early decks. At this point, it is obselete. (IF something strange happens and cards are missing, the code exits to sort it out.)
   - "handvalue" allows the users to be able to see a value for the hand, instead of having to do the math in their head. It creates an empty set and adds values from each card.
   - "validhand" is extra handling for aces so that when a hand with an ace has two values and one goes over 21, it allows the user to play with the hand values below 21.
   - "game_turn" handles all of the actions and printing as the game goes on. A lot of the printed text and user decisions (via input). Also, player busting is handled here. After the player acts, then the dealer will.
   - "game_winner" takes the values of the hands after game_turn() is over and processes them. Whichever hands are higher will be noted as a winner and a point will be added to their class!

   #### Regarding main():

      This function initializes the player and dealer before running a True loop in order for the user to play the game over and over.
      Before the game calls game_turn, it will initialize and shuffle the deck, then it will remove all cards from player hands.
      (A couple of testing times this did NOT happen, and players could have over 2 cards after being dealt)
      Finally, the game ends via an input of STOP, or it loops back around

 ## Extra Code Notes
   - Throughout the code, there are a few "isinstance" checks, which have to exist since aces record two values, and need to be handled specially as a tuple.
   - Many other isinstance checks also exist because 21 is handled as a single integer, instead of a list. I believe this was to only display 21 if a hand has other values from an ace. (Admittedly this code causes some extra complications instead of leaving it as a part of a list)
   - Busted hands are handled as empty lists, so much of the code is handled with "isinstance(hand, list) and not hand" to prove there a hand is invalid.
   - Time.sleep and extra print() have been utilized for extra dramatic effect

   ## Extra Extra Code Breakdown
   - Because busted hands is that because they are not able to be compared via >, they must be handled before everything else. Hence:
   > "if finalhandp is None and finalhandd is None:"

   - Logic to check that the dealer should hit under 17 is listed here:
   > in Dealer: "def should_hit(self):"

   - In "game_winner()", the function cleans the hand if there are multiple hand values to compare just the top potential number:
   > for players: "finalhandp = best(player_hand)"

   - Code loops upon hit/stand action via:
   > "if player_act not in ("h", "s"):"

   - Code can be exited via CTRL + D or CTRL + C at any point:
   > via "except EOFError, KeyboardInterrupt"


   ## Cleanup: Explaining test_project.py

   There are 10 total tests in the pytest file. These tests have been chosen to verify the larger, fundamental aspects of the code to ensure all actions are working as proposed. Many of them are class actions.
   - "test_dealerstand():" uses a proprietary hand to ensure the dealer will stand if hand value is over 17
   - "test_dealerhit():" tests that a dealer will actually hit if its hand is under 17
   - "test_blackjackvalues():" tests that face cards are reassigned to a value of 10
   - "test_blackjackvalues_ace():" tests that aces are assigned (1, 11)
   - "test_deal():" tests that the number of cards dealt matches itself. ("deal(2)" actually deals 2)
   - "test_dealfromdeck():" tests that the cards removes cards from the deck
   - "test_dealnewcards():" tests that the dealt cards are actually no longer in the deck
   - "test_integriddy():" tests the check for a valid deck length to play
   - "test_shuffleorder():" tests that when a deck is shuffled, the new deck is actually different
   - "test_shuffleloss():" tests that no cards are removed when shuffling





