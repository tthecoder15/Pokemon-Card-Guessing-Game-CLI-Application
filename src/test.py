from main import create_rand_card
import json
import os


def test_json_data():
    set_files_list = os.listdir("card_data/")
    print(set_files_list)
    for set_file in set_files_list:
        file_path = "card_data/" + set_file
        with open(file_path) as f:
            all_sets_cards = json.load(f)
        for card in all_sets_cards:
            if card["supertype"] == "Pokémon":
                print(file_path)
                print(card["name"])
                assert card["name"]
                print(card["flavorText"])
                assert card["flavorText"]
                # assert card['convertedRetreatCost'] -> Not neccessary as cards with no retreat cost have no converted retreat cost key
                if "attacks" in card:
                    print(card["attacks"])
                else:
                    print("This Pokémon has no attacks")
                if "abilities" in card:
                    print("abilities")
                else:
                    print("This Pokémon has no abilities")
                # Checks that attacks exist OR card has an ability
                print(card["subtypes"])
                assert card["subtypes"][0]
                print(card["types"])
                assert card["types"]
                print(card["number"])
                assert card["number"]


# def test_create_random_cards():
#     num_of_tests = 5
#     while num_of_tests > 0:
#         card = create_rand_card()
#         print(card)
#         assert card['name']
#         assert card['flav_text']
#         assert card['atks']
#         assert card['stage']
#         assert card['card_types']
#         assert card['set_number']
#         assert card['ret_c']
#         assert card['expansion']
#         num_of_tests -= 1
