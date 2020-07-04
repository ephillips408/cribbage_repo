import random
import itertools
import scoring as score
import declarations as decs

game_player = decs.Player(is_dealer=False)
dummy_player = decs.Player(is_dealer=False) # Allows for a better representation of the odds of what card is flipped.

game_deck = decs.Deck()
game_deck.shuffle()

for i in range(6):
    game_player.hand.append(game_deck.deal_one())
    dummy_player.hand.append(game_deck.deal_one())

for card in game_player.hand:
    print (str(card))

discards = list(input("Enter which cards to discard, separated by a comma: "))
indices = [ int(entry)-1 for entry in discards if entry.isdigit() == True ]

game_player.discard_two(game_player.hand, indices)

flipped_card = game_deck.deal_one()
print (flipped_card)

game_player.hand.append(flipped_card)

val_list = [ card.value for card in game_player.hand ]
straight_rank_list = sorted([ card.straight_rank for card in game_player.hand ])
suit_list = [ card.suit for card in game_player.hand ]

print (suit_list, "\n", val_list, "\n", straight_rank_list)
print (decs.find_score(val_list, straight_rank_list, suit_list))

