class Card:
    def __init__(self, name, flav_text, stage, card_types, set_number, expansion, release_date, atks, ret_c):
        self.name = name
        self.flav_text = flav_text
        self.atks = atks
        self.stage = stage
        self.card_types = card_types
        self.set_number = set_number
        self.expansion = expansion
        self.release_date = release_date
        self.ret_c = ret_c

