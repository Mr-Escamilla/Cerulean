import random

class Card:
  def __init__(self, _suit, _value):
    self.name = f"{_value} {_suit}"
    self.suit = _suit
    self.value = _value
    # if _value in [12, 13, 14]:


  def __str__(self):
    return self.name


def deal_cards(hand_to_give_cards_to, deck):
  random_card = deck.pop(random.randrange(len(deck)))
  hand_to_give_cards_to.append(random_card)

# make the deck
def make_deck():
  deck = []
  for suit in ["H", "D", "C", "S"]:
    for value in [2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10, 10, 11]:
      deck.append(Card(suit, value))

  return deck

still_playing = True
while still_playing:
  deck = make_deck()
  player_hand = []
  dealer_hand = []
  print("Hello! Welcome to blackjack")
  playing_choice = input("Would you like to play? (y/n): ").lower()
  while playing_choice not in ["y", "n"]:
    playing_choice = input("Invalid. Would you like to play blackjack? (y/n): ").lower()

  # shuffle
  random.shuffle(deck)
  deal_cards(player_hand, deck)
  deal_cards(dealer_hand, deck)
  deal_cards(player_hand, deck)
  deal_cards(dealer_hand, deck)

  for cards in player_hand:
    print(cards)
  for cards in dealer_hand:
    print(cards)

  if playing_choice == 'n':
    print("Okay, goodbye!")
    exit()