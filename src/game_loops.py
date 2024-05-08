import os
from numpy import random
from guess import guess
from game_dialogue import hint_dialogue, standard_dialogue

def hint_guess_loop(round_card, session_hints_and_score, dialogue_key):
    print(standard_dialogue[f'{dialogue_key}'])
    while True:
        response = input()
        if response.lower() == "guess" or response.lower() == "'guess'":
            guess(round_card, session_hints_and_score)
        elif response.lower() == "hint" or response.lower() == "'hint'":
            break
        else:
            print("Please type 'guess' or 'hint'." + "\n")
    os.system("clear")


def choose_hint_loop(
    round_card, session_hints_and_score, dialogue_key, hint_choice1, hint_choice2
):
    print(hint_dialogue[f'{dialogue_key}'])
    while True:
        response = input()

        if response.lower() == hint_choice1 or response.lower() == f"'{hint_choice1}'":
            os.system("clear")
            session_hints_and_score.update_hints(
                hint_choice1,
                round_card[f"{hint_choice1}"],
            )
            break

        if response.lower() == hint_choice2 or response.lower() == f"'{hint_choice2}'":
            os.system("clear")
            if hint_choice2 == "attack":
                session_hints_and_score.update_hints(
                    hint_choice2,
                    round_card["atks"][random.randint(0, len(round_card["atks"])) - 1][
                        "name"
                    ],
                )

            elif hint_choice2 == "type":
                session_hints_and_score.update_hints(
                    hint_choice2,
                    round_card["type"][0],
                )

            else:
                session_hints_and_score.update_print_round_hints(
                    hint_choice2,
                    round_card[f"{hint_choice2}"],
                )
            break
        else:
            print(f"Please type '{hint_choice1}' or '{hint_choice2}'." + "\n")
