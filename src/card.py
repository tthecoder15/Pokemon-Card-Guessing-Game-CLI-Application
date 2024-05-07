class Card:
    def __init__(self, name, flavor_text, stage, card_types, set_number, expansion, release_date, atks, ret_cost):
        self.name = name
        self.flavor_text = flavor_text
        self.atks = atks
        self.stage = stage
        self.card_types = card_types
        self.set_number = set_number
        self.expansion = expansion
        self.release_date = release_date
        self.ret_cost = ret_cost

# THE ORIGINAL OBJECT SET UP
# return Card(
#         name=rand_card["name"],
#         stage=rand_card["subtypes"][0],
#         card_types=rand_card["types"],
#         expansion=expansion,
#         release_date=release_date,
#         set_number=rand_card["number"],
#         flavor_text=rand_card["flavorText"],
#         ret_cost=rand_card["convertedRetreatCost"],
#         atks=rand_card["attacks"],
#     )

# ORIGINAL CLASS OBJECT TEST FOR EVERY CARD
# def test_every_cards_creation():
#     # Tests that every "Pokemon" supertype card can be ran through the Card class. Checks that release data and linking to set name data works successfully
#     set_files_list = os.listdir("card_data/")
#     with open('set_data/set_data.json') as f:
#         all_sets_info = json.load(f)      
#     for set_file in set_files_list:
#         file_path = "card_data/" + set_file
        
#         with open(file_path) as f:
#             all_cards_in_set = json.load(f)
        
#         for card in all_cards_in_set:
#             for set in all_sets_info:
#                 if set['id'] == file_path[10:-5]:
#                     expansion = set['name']
#                     print(expansion)
#                     release_date = set['releaseDate']
#                     print(release_date)
#                     break

#             print(f"{card['name']} from {file_path} is being assessed")
#             if card["supertype"] == "Pokémon" and "flavorText" in card:
#                 rand_card = card
#                 if 'convertedRetreatCost' not in rand_card:
#                     rand_card.update({'convertedRetreatCost': '0'})
#                 if 'attacks' not in rand_card:
#                     rand_card.update({'attacks': 'This Pokémon has no attacks!'})
#                 assert Card(
#                     name=rand_card["name"],
#                     stage=rand_card["subtypes"][0],
#                     card_types=rand_card["types"],
#                     expansion=expansion,
#                     release_date=release_date,
#                     set_number=rand_card["number"],
#                     flav_text=rand_card["flavorText"],
#                     ret_c=rand_card["convertedRetreatCost"],
#                     atks=rand_card["attacks"],
#                 )
#             else:
#                 print(f"{card['name']} is not eligible")

