"""Module containing functions to randomly generate Pokémon cards from local json files.

Upon import, loads set data to local variables for later access.
"""

import os
from numpy import random
import json

with open("set_data/set_data.json") as f:
    loaded_sets_info = json.load(f)
available_set_dirs = os.listdir("card_data/")
local_sets_dicts = {}
for loaded_set_dict in loaded_sets_info:
    for set_dir in available_set_dirs:
        if set_dir[:-5] == loaded_set_dict["id"]:
            local_sets_dicts.update(
                {
                    loaded_set_dict["name"]: {
                        "set_name": loaded_set_dict["name"],
                        "set_id": loaded_set_dict["id"],
                        "release_date": loaded_set_dict["releaseDate"],
                        "set_dir": set_dir,
                    }
                }
            )
available_set_names = list(local_sets_dicts.keys())


def gen_rand_card(gametype):
    """Generates a local dict containing a random Pokémon card's data.

    Operates differently depending on gametype.
    Standard gametype prompts user to choose a Pokémon card expansion.
    A random Pokémon card, detailing a particular Pokémon, is returned from this set.
    Hard gametype randomly selects the set and returns a Pokémon's details as a dictionary.

    Parameters
    ----------
    gametype : _str_
        A string, "standard" or "hard", that specfies game type.

    Returns
    -------
    _dict_
        A dict containing the random generated Pokémon card's attributes.
    """
    if gametype == "standard":
        while True:
            print(
                "Please select a Pokémon card expansion for a random card to be chosen from: "
            )
            for index, set_name in enumerate(available_set_names):
                print(f"{index+1}. {set_name}")
            print(
                "\nTo choose, please type the number next to the expansion name and press enter."
            )
            response = input()
            if int(response) <= len(available_set_names):
                selected_set = available_set_names[int(response) - 1]
                break

    elif gametype == "hard":
        random_index = int(random.randint(len(available_set_names)))
        selected_set = available_set_names[random_index]

    with open(f"card_data/{local_sets_dicts[selected_set]['set_dir']}") as f:
        loaded_set_cards = json.load(f)

    while True:
        rand_int = random.randint(len(loaded_set_cards))
        rand_card = loaded_set_cards[rand_int]
        # Randomly generates an integer, selects the card at that and copies it to a local variable.
        if rand_card["supertype"] == "Pokémon" and "flavorText" in rand_card:
            break
        # Evaluates if that card is a Pokemon card with flavor text then breaks the loop.
    if "convertedRetreatCost" not in rand_card:
        rand_card.update({"convertedRetreatCost": "0"})
        # Evaluates if the card has a "convertedRetreatCost" key and if not assigns it a value of 0.
    if "attacks" not in rand_card:
        rand_card.update({"attacks": "This Pokémon has no attacks!"})
        # Evaluates if the card has an "attacks" key and if not assigns it a value.
    return {
        "name": rand_card["name"],
        "stage": rand_card["subtypes"][0],
        "card_types": rand_card["types"],
        "expansion": local_sets_dicts[selected_set]["set_name"],
        "release_date": local_sets_dicts[selected_set]["release_date"],
        "set_number": rand_card["number"],
        "flavor_text": rand_card["flavorText"],
        "retreat": str(rand_card["convertedRetreatCost"]),
        "atks": rand_card["attacks"],
        "type": rand_card["types"],
    }
