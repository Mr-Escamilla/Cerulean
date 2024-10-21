import random
deck_of_cards = []

for i in range(13): #0-12            # add values to the deck of cards 0-12
  deck_of_cards.append(i + 1) # [].append(1) -> [1]
  deck_of_cards.append(i + 1) # [1].append(1) -> [1, 1]
  deck_of_cards.append(i + 1)
  deck_of_cards.append(i + 1)

print(deck_of_cards)
random.shuffle(deck_of_cards) # Shuffle the deck
print(deck_of_cards)

piles = [[] for i in range(13)] # Make 13 piles
print(piles)

for card in deck_of_cards:  # Go through every card
  piles[card - 1].append(card)  #add card to its own pile
print(piles)

deck_of_cards = []
for pile in piles:  # For every pile
  deck_of_cards.extend(pile) # stack the piles back into a deck
print(deck_of_cards)