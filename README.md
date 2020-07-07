# Cribbage Score Calculator

This is a program that can calculate the score of a cribbage hand, assuming that the player is not the dealer. His nob scoring still needs to be added. The first functionality change that I would like to make in the near future is the ability for the player to add their choices to a SQL database.

Second Commit:
    Fixed a bug with the find_flush function.

Third Commit:
    Added the ability to play multiple times. Also, added the play_options.py file for future play options, and to make sure that the game_logic file does not become too cluttered.

Fourth Commit:
    Altered the player_not_dealer function to force the discard of two cards. Also, cleaned up the run_game function in game_logic.py, and fixed a bug where the non-dealer player chose their discards with a higher number followed by a lower number.