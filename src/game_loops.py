"""A collection of looping functions used in gameplay.

------
PlayAgain
    An exception raised to trigger another round of gameplay.
Menu
    An exception raised to return the user to the menu.
HintAdded
    An exception raised to break the hint updating loop.

"""

import os
from numpy import random
from guess import guess, CorrectGuess, IncorrectGuess
from game_dialogue import hint_dialogue, gameplay_dialogue


class Menu(Exception):
    """An exception raised to return the user to the menu."""


class PlayAgain(Exception):
    """An exception raised to trigger another round of gameplay."""


class HintAdded(Exception):
    """An exception raised to break the hint updating loop."""


def play_again_loop():
    """Prompts the user to play again or return to the main menu.

    Raises
    ------
    PlayAgain
        If the user inputs 'play again', returns the user to the game initialising loop.
    Menu
        If the user inputs 'menu', returns the user to the main menu loop.
    """
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
    """Initiated the guess function then prompts the user to play again or quit.

    Parameters
    ----------
    round_card : _dict_
        The mystery card's dict storing the card's data.
    session_hints_score : _class instance_
        The HintsAndScore instance tracking the user's hints.
    scoreboard : _class instance_
        The Scoreboard instance tracking the user's session ID and scoreboard.
    """
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
    """A loop that prompts the user to choose hint or guess.

    Parameters
    ----------
    round_card : _dict_
        The mystery card's dict storing the card's data.
    session_hints_score : _class instance_
        The HintsAndScore instance tracking the user's hints.
    scoreboard : _class instance_
        The Scoreboard instance tracking the user's session ID and scoreboard.
    dialogue_key : _dict key value_
        A dictonary key value corresponding to which hint the user would be selecting.
    """
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
    """Matches the users hint choice to the card attribute and adds it to a HintsAndScore instance.

    Parameters
    ----------
    round_card : _dict_
        The mystery card's dict storing the card's data.
    session_hints_score : _class instance_
        The HintsAndScore instance tracking the user's hints.
    hint_type : _dict key_
        A dict key value that corresponds to the round card's attributes.
    response : _input_
        _The user's input responding to the prompt._

    Raises
    ------
    HintAdded
        Notes that the hint has been added and returns the user to the gameplay function.
    """
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
    """Prompts the user to choose an appropriate hint.

    Parameters
    ----------
    round_card : _dict_
        The mystery card's dict storing the card's data.
    session_hints_score : _class instance_
        The HintsAndScore instance tracking the user's hints.
    dialogue_key : _dict key value_
        A dictonary key value corresponding to which hint the user would be selecting.
    hint_choice1 : _dict key val_
        One of the hints that the user is choosing from.
    hint_choice2 : _dict key val_
        One of the hints that the user is choosing from.
    """
    print(hint_dialogue[f"{dialogue_key}"])
    while True:
        response = input()
        try:
            hint_check(round_card, session_hints_score, hint_choice1, response)
            hint_check(round_card, session_hints_score, hint_choice2, response)
            print(f"Please type '{hint_choice1}' or '{hint_choice2}'." + "\n")
        except HintAdded:
            break
