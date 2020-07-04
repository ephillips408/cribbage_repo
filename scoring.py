import random
import itertools

def find_fifteens(list):

    scoring_sum = 15
    fifteen_score = 0
    for L in range (0, len(list) + 1):
        # Find all combinations in the hand
        for subset in itertools.combinations(list, L):
            # Checks for sum of 15 for each subset
            b = sum(int(i) for i in subset)
            if b == scoring_sum:
                fifteen_score += 2
    return fifteen_score

def find_matches(list):

    matches_found = False
    no_matches = False
    score = 0

    while matches_found == False or no_matches == False:

        four_of_a_kind = [ set(comb) for comb in itertools.combinations(list, 4) ]

        for comb in four_of_a_kind:

            if len(comb) == 1:
                score += 12
                matches_found = True
                return score

        three_of_a_kind = [ set(comb) for comb in itertools.combinations(list, 3) ]

        for comb in three_of_a_kind:

            if len(comb) == 1:
                score += 6

        pairs = [ set(comb) for comb in itertools.combinations(list, 2) ]

        for comb in pairs:

            if len(comb) == 1 and comb not in three_of_a_kind:
                score += 2
        
        if score != 0:
            matches_found = True
            return score

        else:
            no_matches = True
            return score

def find_straights(list):

    score = 0
    found_straight = False
    no_straights = False

    while found_straight == False or no_straights == False:

        unique_elements = sorted(set(list))
        # If all of the elements in the set are unique, and the last number is equal to 4 plus the first number, the set is a straight of length 5.
        if len(unique_elements) == len(list) and unique_elements[-1] == unique_elements[0] + 4:
            score += 5
            found_straight = True 
            return score

        # Using the set method removes duplicates in combinations of 4 and 3.
        four_combs = [ sorted(set(comb)) for comb in itertools.combinations(list, 4) ]
        three_combs = [ sorted(set(comb)) for comb in itertools.combinations(list, 3) ]

        for ele in four_combs:
            if len(ele) != 4: pass
            elif len(ele) == 4 and ele[-1] != ele[0]+3: pass
            else: score += 4

        if score != 0:
            found_straight = True
            return score

        else:

            for ele in three_combs:
                if len(ele) != 3: pass
                elif len(ele) == 3 and ele[-1] != ele[0]+2: pass
                else: score += 3

            if score != 0:
                found_straight = True
                return score

            else:
                no_straights = True
                return score

def find_flush(list):

    score = 0
    
    if list[3::-1] == list[0:-1]: score += 4
    if list[::-1] == list[0::] and score != 0: score += 1

    return score

val_test_hand = [10,10,5,5,10]
straight_rank_test_hand = sorted([5,7,10,12,13])
test_flush = ["D", "D", "D", "D", "C"]
