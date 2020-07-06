import declarations as decs

def player_not_dealer(player_one, player_two, deck):
    #Player one is the player, player_two is the dummy.

    for i in range(6):
        player_one.hand.append(deck.deal_one())
        player_two.hand.append(deck.deal_one())

    for card in player_one.hand:
        print (str(card))

    discards = list(input("Enter which cards to discard, separated by a comma: "))
    indices = [ int(entry)-1 for entry in discards if entry.isdigit() == True ]

    player_one.discard_two(player_one.hand, indices)

    flipped_card = deck.deal_one()
    print (flipped_card)

    player_one.hand.append(flipped_card)

    val_list = [ card.value for card in player_one.hand ]
    straight_rank_list = sorted([ card.straight_rank for card in player_one.hand ])
    suit_list = [ card.suit for card in player_one.hand ]

    print (suit_list, "\n", val_list, "\n", straight_rank_list)
    print (decs.find_score(val_list, straight_rank_list, suit_list))

    play_again = input("Play again (y/n)? ")

    if play_again == 'y': return play_again
    else: pass