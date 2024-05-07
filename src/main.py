import json
import os
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
        'ret_cost' : str(rand_card["convertedRetreatCost"]),
        'atks' : rand_card["attacks"],
        'type' : rand_card['types']}


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


round_hints = {}

def guess():
    print("This will trigger the guessing component of the game")
    raise Exception("Guessing function not yet defined")

def hard_mode_game():
    print("This will trigger the hard mode of the game")
    raise Exception("Hard mode function not yet defined")

def scoreboard():
    print("This will trigger the scoreboard functionality")
    raise Exception("Scoreboard functionality not defined yet")

def update_print_round_hints(hint_label, dialogue, hint):
    key_value = dialogue + '\n' + '"' + hint + '"' + '\n'
    round_hints.update({hint_label : key_value})
    return print(round_hints[hint_label])

def hint_reminder(*hints_received):
    print(standard_dialogue['summary'] + '\n')
    for hint in hints_received:
        print(round_hints[hint])

def standard_game():
    os.system('clear')

    print(menu['greeting'])
    while True:
        response = input()
        if response.lower() == "scoreboard" or response.lower() == "'scoreboard'":
        # Need to return scoreboard here
            scoreboard()
    
        else:
            break

    os.system('clear')        
    print(menu['mode_choice'])            
    
    while True:
        response = input()
        if response.lower() == "hard" or response.lower() == "'hard'":
        # Need to run hardmode here
            hard_mode_game()
        
        else:
            break
    
    os.system('clear')
    round_card = gen_rand_card()
    update_print_round_hints('hint_1', standard_dialogue['hint_1'], round_card['flavor_text'])
    
    print(standard_dialogue['guess_or_hint1'])
    while True:       
        response = input()
        if response.lower() == 'guess' or response.lower() == "'guess'":
            guess()
        
        elif response.lower() == 'hint' or response.lower() == "'hint'":
            break

        else:
            print("\n" + "Please type 'guess' or 'hint'." + "\n")    
    os.system('clear')
    
    print(standard_dialogue['2nd_hint_prompt'])
    while True:
        response = input()
        
        if response.lower() == 'retreat cost' or response.lower() == "'retreat cost'":         
            os.system('clear')
            update_print_round_hints('hint_2', standard_dialogue['2nd_hint_retreat'], round_card['ret_cost'])
            break

        if response.lower() == 'attack' or response.lower() == "'attack'":         
            os.system('clear')
            update_print_round_hints('hint_2', standard_dialogue['2nd_hint_attack'], round_card['atks'][random.randint(0, len(round_card['atks']))-1]['name'])
            break

        else:
            print("\n" + "Please type 'retreat cost' or 'attack'." + "\n")


    hint_reminder('hint_1')
    print(standard_dialogue['guess_or_hint2'])
    while True:
        response = input()
        if response.lower() == 'guess' or response.lower() == "'guess'":
            guess()
        
        elif response.lower() == 'hint' or response.lower() == "'hint'":
            break

        else:
            print("\n" + "Please type 'guess' or 'hint'." + "\n")
    os.system('clear')

    print(standard_dialogue['3rd_hint_prompt'])
    while True:
        response = input()
        
        if response.lower() == 'evolution' or response.lower() == "'evolution'":         
            os.system('clear')
            update_print_round_hints('hint_3', standard_dialogue['3rd_hint_stage'], round_card['stage'])
            break

        if response.lower() == 'type' or response.lower() == "'type'":         
            os.system('clear')
            update_print_round_hints('hint_3', standard_dialogue['3rd_hint_type'], round_card['type'][0])
            break

        else:
            print("\n" + "Please type 'retreat cost' or 'attack'." + "\n")

    hint_reminder('hint_1', 'hint_2')
    print(standard_dialogue['guess_time'])
    guess()

# print(gen_rand_card())
standard_game()