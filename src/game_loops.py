import os
from numpy import random
from guess import guess, CorrectGuess, IncorrectGuess
from game_dialogue import hint_dialogue, gameplay_dialogue


class Menu(Exception):
    pass


class PlayAgain(Exception):
    pass


class HintAdded(Exception):
    pass


def play_again_loop():
    while True:
        response = input()
        if response.lower() == "play again" or response.lower() == "'play again'":
            os.system("clear")
            raise PlayAgain
        elif response.lower() == "menu" or response.lower() == "'menu'":
            raise Menu
        else:
            print(gameplay_dialogue["play_again_loop"])


def guess_loop(round_card, session_hints_score, scoreboard):
    try:
        guess(
            round_card,
            session_hints_score,
            scoreboard,
        )
    except CorrectGuess:
        print(gameplay_dialogue["correct_play_again"])
        play_again_loop()
    except IncorrectGuess:
        print(gameplay_dialogue["incorrect_play_again"])
        play_again_loop()


def hint_guess_loop(round_card, session_hints_score, scoreboard, dialogue_key):
    print(gameplay_dialogue[f"{dialogue_key}"])
    while True:
        response = input()
        if response.lower() == "guess" or response.lower() == "'guess'":
            guess_loop(round_card, session_hints_score, scoreboard)
        elif response.lower() == "hint" or response.lower() == "'hint'":
            break
        else:
            print("Please type 'guess' or 'hint'." + "\n")
    os.system("clear")


def hint_check(round_card, session_hints_score, hint_type, response):
    if response.lower() == hint_type or response.lower() == f"'{hint_type}'":
        if hint_type == "attack":
            session_hints_score.update_hints(
                hint_type,
                round_card["atks"][random.randint(0, len(round_card["atks"])) - 1][
                    "name"
                ],
            )
            raise HintAdded
        elif hint_type == "type":
            session_hints_score.update_hints(
                hint_type,
                round_card["type"][0],
            )
            raise HintAdded
        elif hint_type == "stage":
            session_hints_score.update_hints(
                hint_type,
                round_card["stage"],
            )
            print(hint_dialogue["stage_reminder"])
            raise HintAdded
        else:
            session_hints_score.update_hints(
                hint_type,
                round_card[hint_type],
            )
            raise HintAdded


def choose_hint_loop(
    round_card, session_hints_score, dialogue_key, hint_choice1, hint_choice2
):
    print(hint_dialogue[f"{dialogue_key}"])
    hint_added = False
    while True:
        response = input()
        try:
            hint_check(
                round_card, session_hints_score, hint_choice1, response
            )
            hint_check(
                round_card, session_hints_score, hint_choice2, response
            )
            print(f"Please type '{hint_choice1}' or '{hint_choice2}'." + "\n")
        except HintAdded:
            break
