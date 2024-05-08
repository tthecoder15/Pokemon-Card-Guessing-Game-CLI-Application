import os
from numpy import random
from guess import guess
from game_dialogue import standard_dialogue, hint_dialogue
from random_card_gen import gen_rand_card
from round_hints import hint_reminder, update_print_round_hints

round_hints = {}


def hint_guess_loop(round_card, dialogue):
    print(dialogue)
    while True:
        response = input()
        if response.lower() == "guess" or response.lower() == "'guess'":
            guess(round_card)

        elif response.lower() == "hint" or response.lower() == "'hint'":
            break

        else:
            print("\n" + "Please type 'guess' or 'hint'." + "\n")
    os.system("clear")


def which_hint(
    round_card, round_hints, hint_number, dialogue, hint_choice1, hint_choice2
):
    print(dialogue)
    while True:
        response = input()

        if response.lower() == hint_choice1 or response.lower() == f"'{hint_choice1}'":
            os.system("clear")
            update_print_round_hints(
                round_hints,
                hint_number,
                hint_dialogue[f"{hint_choice1}"],
                round_card[f"{hint_choice1}"],
            )
            break

        if response.lower() == hint_choice2 or response.lower() == f"'{hint_choice2}'":
            os.system("clear")
            if hint_choice2 == "attack":
                update_print_round_hints(
                    round_hints,
                    hint_number,
                    hint_dialogue[f"{hint_choice2}"],
                    round_card["atks"][random.randint(0, len(round_card["atks"])) - 1][
                        "name"
                    ],
                )

            elif hint_choice2 == "type":
                update_print_round_hints(
                    round_hints,
                    hint_number,
                    hint_dialogue[f"{hint_choice2}"],
                    round_card["type"][0],
                )

            else:
                update_print_round_hints(
                    round_hints,
                    hint_number,
                    hint_dialogue[f"{hint_choice2}"],
                    round_card[f"{hint_choice2}"],
                )
            break
        else:
            print("\n" + f"Please type '{hint_choice1}' or '{hint_choice2}'." + "\n")


def standard_game():
    round_hints = {}
    os.system("clear")
    round_card = gen_rand_card()
    update_print_round_hints(
        round_hints, "hint_1", hint_dialogue["hint_1"], round_card["flavor_text"]
    )

    hint_guess_loop(round_card, standard_dialogue["guess_or_hint1"])
    which_hint(
        round_card,
        round_hints,
        "hint_2",
        hint_dialogue["2nd_hint_prompt"],
        "retreat",
        "attack",
    )
    hint_reminder(round_hints, "hint_1")

    hint_guess_loop(round_card, standard_dialogue["guess_or_hint2"])
    which_hint(
        round_card,
        round_hints,
        "hint_3",
        hint_dialogue["3rd_hint_prompt"],
        "stage",
        "type",
    )
    hint_reminder(round_hints, "hint_1", "hint_2")

    print(standard_dialogue["guess_time"])
    guess(round_card)


# print(gen_rand_card())
# standard_game()
