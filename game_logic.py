import scoring as score
import declarations as decs
import play_options as play
import os
import sys

def run_game():

    while True:

        player_type = input("Play as the dealer ('D') or not dealer ('ND')? To exit, type 'stop': ")

        if player_type == 'ND':
            
            game_player.is_dealer = False
            dummy_player.is_dealer = False # Allows for a better representation of the odds of what card is flipped.
            break

        elif player_type == 'D':

            game_player.is_dealer = True
            dummy_player.is_dealer = False
            print ("Not yet supported.")
            continue

        elif player_type == 'stop':

            break

        else:

            print ("Unrecognized input.")            

    if game_player.is_dealer == False:

        test = play.player_not_dealer(game_player, dummy_player, game_deck)
        if test == 'y': os.execl(sys.executable, sys.executable, * sys.argv) # This restarts the file from the beginning.
        else: pass

game_player = decs.Player()
dummy_player = decs.Player()
game_deck = decs.Deck()
game_deck.shuffle()

run_game()
