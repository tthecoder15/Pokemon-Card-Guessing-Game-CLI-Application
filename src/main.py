import json
from numpy import random
from game_dialogue import standard_dialogue, menu

with open("card_data/base1.json") as f:
    # PRESENTLY loads the base1.json file to ```all_sets_cards``` local variable
    # Random set loading available in test.py
    all_sets_cards = json.load(f)
    # PRESENTLY sets the ```loaded_card_set_id``` local var to base1 for use in creating the expansion release date data
    loaded_card_set_id = "base1"

with open("set_data/set_data.json") as f:
    # Loads set data file, matches set['id'] value to variable ```loaded_card_set_id``` previously declared, then copies set['name'] and set['releaseDate'] from the Data JSON to local variable for passing to the creator class called later
    all_sets_info = json.load(f)
    for set in all_sets_info:
        if set["id"] == loaded_card_set_id:
            expansion = set["name"]
            release_date = set["releaseDate"]
            break


def gen_rand_card():
    while True:
        # Randomly generates an integer within the set selected's length then selects that dict within the set and copies it to a local variable. Evaluates if that card is a Pokemon card with flavor text then breaks the loop.
        rand_int = random.randint(len(all_sets_cards))
        rand_card = all_sets_cards[rand_int]
        if rand_card["supertype"] == "Pokémon" and "flavorText" in rand_card:
            break
        # Evaluates if the card has a "convertedRetreatCost" key and if not assigns it a value of 0
    if "convertedRetreatCost" not in rand_card:
        rand_card.update({"convertedRetreatCost": "0"})
        # Evaluates if the card has an "attacks" key and if not assigns it a value of "This Pokemon has no attacks!"
    if "attacks" not in rand_card:
        rand_card.update({"attacks": "This Pokémon has no attacks!"})

        # RETURNS dict using randomly generated cards info
    return {'name' : rand_card["name"],
        'stage' : rand_card["subtypes"][0],
        'card_types' : rand_card["types"],
        'expansion' : expansion,
        'release_date' : release_date,
        'set_number' : rand_card["number"],
        'flavor_text' : rand_card["flavorText"],
        'ret_cost' : rand_card["convertedRetreatCost"],
        'atks' : rand_card["attacks"]}


# execution
# card = gen_rand_card()
# print(card['flavor_text'])

# GAME TRACKER CLASS IF NEEDED
# class Game_Tracker():
#     def __init__(self):
#         self._games = 1

#     @property
#     def games(self):
#         return self._games
    
#     @games.setter
#     def games(self):
#         self._games += 1
    
#     @games.getter
#     def games(self):
#         return self._games


round_clues =[]

def standard_game():
    if input(menu['greeting']).lower() == "scoreboard":
        # Need to return scoreboard here
        print("THIS WILL SHOW THE SCOREBOARD")
        return
    if input(menu['mode_choice']).lower() == "hard":
        # Need to run hardmode here
        print("THIS WILL RUN HARDMODE")
        return
    
    round_card = gen_rand_card()
    print(standard_dialogue['hint_1'])
    print(round_card['flavor_text'])


standard_game()