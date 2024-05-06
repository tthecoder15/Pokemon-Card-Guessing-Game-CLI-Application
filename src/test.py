from main import gen_rand_card
from card import Card
import json
import os


def test_json_data():
    set_files_list = os.listdir("card_data/")
    print(set_files_list)
    for set_file in set_files_list:
        file_path = "card_data/" + set_file
        with open(file_path) as f:
            all_cards_in_set = json.load(f)
        for card in all_cards_in_set:
            if card["supertype"] == "Pokémon":
                print(file_path)
                print(card["name"])
                assert card["name"]
                if "flavorText" in card:
                    print(card["flavorText"])
                else:
                    print(f"{card['name']} in {file_path} has no flavour text")
                if "attacks" in card:
                    assert card["attacks"]
                else:
                    print(f"{card['name']} has no attacks")
                if "abilities" in card:
                    assert card["abilities"]
                else:
                    print(f"{card['name']} has no abilities")
                # Checks that attacks exist OR card has an ability
                print(card["subtypes"])
                assert card["subtypes"][0]
                print(card["types"])
                assert card["types"]
                print(card["number"])
                assert card["number"]


def test_every_cards_creation(monkeypatch):
    set_files_list = os.listdir("card_data/")
    for set_file in set_files_list:
        file_path = "card_data/" + set_file
        with open(file_path) as f:
            all_cards_in_set = json.load(f)
        for card in all_cards_in_set:
            print(f"{card['name']} from {file_path} is being assessed")
            if card["supertype"] == "Pokémon" and "flavorText" in card:
                rand_card = card
                if 'convertedRetreatCost' not in rand_card:
                    rand_card.update({'convertedRetreatCost': '0'})
                if 'attacks' not in rand_card:
                    rand_card.update({'attacks': 'This Pokémon has no attacks!'})
                assert Card(
                    name=rand_card["name"],
                    stage=rand_card["subtypes"][0],
                    card_types=rand_card["types"],
                    expansion="base1",
                    set_number=rand_card["number"],
                    flav_text=rand_card["flavorText"],
                    ret_c=rand_card["convertedRetreatCost"],
                    atks=rand_card["attacks"],
                )
            else:
                print(f"{card['name']} is not eligible")