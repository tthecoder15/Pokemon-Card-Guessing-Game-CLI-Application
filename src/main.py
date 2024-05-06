import json
from numpy import random
from card import Card

# x = random.randomint(max number)
# card_data_paths = os.listdir('card_data/')
# print(card_data_paths)

with open("card_data/base1.json") as f:
    set_loaded = "base1"
    # When different set logic is instilled, path str -'.json' will be set_loaded
    all_sets_cards = json.load(f)

def gen_rand_card():
    # while True:
    #     rand_int = random.randint(len(all_sets_cards))
    #     rand_card = all_sets_cards[rand_int]
    #     if rand_card["supertype"] == "Pokémon" and 'flavorText' in rand_card:
    #         break

    rand_card = all_sets_cards[16]
    if 'convertedRetreatCost' not in rand_card:
        rand_card.update({'convertedRetreatCost': '0'})
    if 'attacks' not in rand_card:
        rand_card.update({'attacks': 'This Pokémon has no attacks!'})
    return Card(
        name=rand_card["name"],
        stage=rand_card["subtypes"][0],
        card_types=rand_card["types"],
        expansion="base1",
        set_number=rand_card["number"],
        flav_text=rand_card["flavorText"],
        ret_c=rand_card["convertedRetreatCost"],
        atks=rand_card["attacks"],
    )


# execution
card=gen_rand_card()
print(gen_rand_card().__dict__)
print(card.__dict__)
