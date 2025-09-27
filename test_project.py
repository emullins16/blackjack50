import pytest
from project import Dealer, Card, Deck

def test_dealerstand():
    dealer = Dealer()
    dealer.hand = [Card("Jack", "Hearts"), Card("Queen", "Hearts")]
    assert dealer.should_hit() == False

def test_dealerhit():
    dealer = Dealer()
    dealer.hand = [Card("Ace", "Hearts"), Card("5", "Hearts")]
    assert dealer.should_hit() == True

def test_blackjackvalues():
    card = Card("Jack", "Hearts")
    assert card.blackjack_values() == 10

def test_blackjackvalues_ace():
    card = Card("Ace", "Hearts")
    assert card.blackjack_values() == (1, 11)

def test_deal():
    deck = Deck()
    deal = deck.deal(2)

    assert len(deal) == 2

def test_dealfromdeck():
    deck = Deck()
    oglength = len(deck.cards)
    deck.deal(2)
    assert len(deck.cards) == oglength - 2

def test_dealnewcards():
    deck = Deck()
    deal = deck.deal(2)

    for card in deal:
            assert card not in deck.cards

def test_integriddy():
    deck = Deck()
    assert len(deck.cards) == 52

def test_shuffleorder():
    deck = Deck()
    ogdeck = deck.cards.copy()
    deck.shuffle()

    assert deck.cards != ogdeck

def test_shuffleloss():
    deck = Deck()
    ogdeck = deck.cards
    deck.shuffle()

    assert set(deck.cards) == set(ogdeck)



