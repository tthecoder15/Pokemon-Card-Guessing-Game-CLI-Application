from game_dialogue import guess_dialogue
import os


class CorrectGuess(Exception):
    pass


class IncorrectGuess(Exception):
    pass


def alt_pokemon_name_check(round_card, response):
    if "Dark" in round_card["name"]:
        if response == round_card["name"][5:]:
            return True
    elif "♂" in round_card["name"] or "♀" in round_card["name"]:
        if response == round_card["name"][:-2]:
            return True


def typo_eval(round_card, response):
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
