"""Contains functions relating to guess

Raises
------
CorrectGuess
    Used to break guess loop and return to play again or menu loops.
IncorrectGuess
    Used to break guess loop and return to play again or menu loops.
"""

import os
from game_dialogue import guess_dialogue


class CorrectGuess(Exception):
    """Used to break guess loop after a correct guess and return to play again or menu loop."""


class IncorrectGuess(Exception):
    """Used to break guess loop after an incorrect guess and return to play again or menu loop."""


def alt_pokemon_name_check(round_card, response):
    """Used to check for card names that contain extra styling.

    Parameters
    ----------

    round_card : _dict_
        The mystery card's dict storing the card's data.
    response : _input_
        The user's guess input.

    Returns
    -------
    _bool_
        Returns true if the card features "Dark" or "♂" or "♀" in name attribute.
    """
    if "Dark" in round_card["name"]:
        if response == round_card["name"][5:]:
            return True
    elif "♂" in round_card["name"] or "♀" in round_card["name"]:
        if response == round_card["name"][:-2]:
            return True


def typo_eval(round_card, response):
    """Evaluates user's guess to see if they may have a typo.

    Parameters
    ----------
    round_card : _dict_
        The mystery card's dict storing the card's data.
    response : _input_
        The user's guess input.

    Returns
    -------
    _bool_
        If the user's guess is not close, the check returns false.
    """
    same_letters_score = 0
    for index, letter in enumerate(round_card["name"]):
        # enumerates each letter in the card's name whilst iterating through each letter
        if index == 0 and len(response) > 0:
            if letter == response[index]:
                # checks if the first letter of the guess and card name are the same
                same_letters_score = 1
        elif index > 0:
            # for any letter besides the first
            try:
                if (
                    letter == response[index]
                    or letter == response[index + 1]
                    or letter == response[index - 1]
                ):
                    # checks if the letter at the same index, 1 infront or 1 behind is the same as the letter being iterated through and adds points to the similarity score
                    same_letters_score += 1
            except IndexError:
                break
    closeness_score = same_letters_score / len(round_card["name"])

    if closeness_score > 0.5:
        os.system("clear")
        print(
            guess_dialogue["close_guess"]
            + response
            + ". \nTry again or press enter to try again: "
        )
    else:
        return False


def guess(round_card, session_hints_score, scoreboard):
    """Prompts user to guess the mystery Pokemon and evaluates if they are correct.

    Parameters
    ----------
    round_card : _dict_
        The mystery card's dict storing the card's data.
    session_hints_score : _class instance_
        The HintsAndScore instance tracking the user's hints.
    scoreboard : _class instance_
        The Scoreboard instance tracking the user's session ID and scoreboard.

    Raises
    ------
    CorrectGuess
        Raised if the user is correct, returns the user to the "play again" or "menu" loop.
    IncorrectGuess
        Raised if the user is incorrect, returns the user to the "play again" or "menu" loop.
    """
    os.system("clear")
    session_hints_score.hint_reminder()
    print(guess_dialogue["guess_prompt"])
    while True:
        response = input().title()
        if (
            response == round_card["name"]
            or alt_pokemon_name_check(round_card, response) is True
        ):
            print(guess_dialogue["answer_correct"])
            session_hints_score.update_score()
            scoreboard.update(session_hints_score.get_score())
            session_hints_score.streak_and_score(correct=True)
            raise CorrectGuess
        else:
            if typo_eval(round_card, response) is False:
                print(guess_dialogue["answer_incorrect"])
                print(
                    f"\nYou guessed: {response}, but the answer was {round_card['name']}!"
                )
                scoreboard.update(session_hints_score.get_score())
                session_hints_score.streak_and_score(correct=False)
                session_hints_score.reset_streak_score()
                raise IncorrectGuess
