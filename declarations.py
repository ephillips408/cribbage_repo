import random
import itertools
import scoring as score

values = {
    "Ace": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,   
}

straight_ranks = {
    "Ace": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13, 
}

suits = ("H", "D", "S", "C")
ranks = ( "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.straight_rank = straight_ranks[rank]

    def __str__(self):
        return f"{self.rank}:{self.suit}"

class Deck:
    
    def __init__(self):

        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        
        return self.all_cards.pop()

class Player:

    def __init__(self, is_dealer):

        self.hand = []
        self.is_dealer = is_dealer
        self.score = 0

    def discard_two(self, list, indices):

        rev_indices = indices[::-1] #Reversed to allow for accurately deleting list elements.
        for entry in rev_indices:
            del list[entry]

def find_score(list_one, list_two, list_three):
    
    #list_one will represent the value list, list two will represent the straight rank list, and list three is the suit list
    points = score.find_fifteens(list_one) + score.find_matches(list_two) + score.find_straights(list_two) + score.find_flush(list_three)
    return points
