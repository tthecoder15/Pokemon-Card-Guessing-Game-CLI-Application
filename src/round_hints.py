from game_dialogue import hint_dialogue

def update_print_round_hints(round_hints, hint_label, dialogue, hint):
    key_value = dialogue + "\n" + '"' + hint + '"' + "\n"
    round_hints.update({hint_label: key_value})
    return print(round_hints[hint_label])

def hint_reminder(round_hints, *hints_received):
    print(hint_dialogue["summary"] + "\n")
    for hint in hints_received:
        print(round_hints[hint])