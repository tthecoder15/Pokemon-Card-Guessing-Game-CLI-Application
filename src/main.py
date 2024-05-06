import json
from numpy import random
from card import Card

# x = random.randomint(max number)
# TO generate list of paths for loading from JSON:
    # card_data_paths = os.listdir('card_data/')
    # print(card_data_paths)

# NEED to develop SET TYPE LOGIC

with open("card_data/base1.json") as f:
    all_sets_cards = json.load(f)
    loaded_card_set_id = 'base1'

with open('set_data/set_data.json') as f:
    all_sets_info = json.load(f)
    for set in all_sets_info:
        if set['id'] == loaded_card_set_id:
            expansion = set['name']
            release_date = set['releaseDate']
            break
    

def gen_rand_card():
    while True:
        rand_int = random.randint(len(all_sets_cards))
        rand_card = all_sets_cards[rand_int]
        if rand_card["supertype"] == "Pokémon" and 'flavorText' in rand_card:
            break
        
    if 'convertedRetreatCost' not in rand_card:
        rand_card.update({'convertedRetreatCost': '0'})
    if 'attacks' not in rand_card:
        rand_card.update({'attacks': 'This Pokémon has no attacks!'})
    return Card(
        name=rand_card["name"],
        stage=rand_card["subtypes"][0],
        card_types=rand_card["types"],
        expansion=expansion,
        release_date=release_date,
        set_number=rand_card["number"],
        flav_text=rand_card["flavorText"],
        ret_c=rand_card["convertedRetreatCost"],
        atks=rand_card["attacks"],
    )


# execution
card=gen_rand_card()
print(gen_rand_card().__dict__)
print(card.__dict__)
