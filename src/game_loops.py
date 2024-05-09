import os
from numpy import random
from guess import guess, CorrectGuess, IncorrectGuess
from game_dialogue import hint_dialogue, standard_dialogue

class Quit(Exception):
    pass

class PlayAgain(Exception):
    pass

def play_again_loop():
    while True:
        response = input()
        if response.lower() == "play again" or response.lower() == "'play again'":
            raise PlayAgain()
        elif response.lower() == "quit" or response.lower() == "'quit'":
            raise Quit()
        else:
            print(standard_dialogue['play_again_loop'])

def guess_loop(round_card, round_hints_session_score):
    try: 
        guess(round_card, round_hints_session_score)
    except CorrectGuess:
        round_hints_session_score.streak_and_score(correct=True)
        print(standard_dialogue['correct_play_again'])
        play_again_loop()
    except IncorrectGuess:
        round_hints_session_score.streak_and_score(correct=False)
        print(standard_dialogue['incorrect_play_again'])
        play_again_loop() 

def hint_guess_loop(round_card, round_hints_session_score, dialogue_key):
    print(standard_dialogue[f'{dialogue_key}'])
    while True:
        response = input()
        if response.lower() == "guess" or response.lower() == "'guess'":
            guess_loop(round_card, round_hints_session_score)
        elif response.lower() == "hint" or response.lower() == "'hint'":
            break
        else:
            print("Please type 'guess' or 'hint'." + "\n")
    os.system("clear")
    
def choose_hint_loop(
    round_card, round_hints_session_score, dialogue_key, hint_choice1, hint_choice2
):
    print(hint_dialogue[f'{dialogue_key}'])
    while True:
        response = input()

        if response.lower() == hint_choice1 or response.lower() == f"'{hint_choice1}'":
            os.system("clear")
            round_hints_session_score.update_hints(
                hint_choice1,
                round_card[f"{hint_choice1}"],
            )
            break

        if response.lower() == hint_choice2 or response.lower() == f"'{hint_choice2}'":
            os.system("clear")
            if hint_choice2 == "attack":
                round_hints_session_score.update_hints(
                    hint_choice2,
                    round_card["atks"][random.randint(0, len(round_card["atks"])) - 1][
                        "name"
                    ],
                )

            elif hint_choice2 == "type":
                round_hints_session_score.update_hints(
                    hint_choice2,
                    round_card["type"][0],
                )

            else:
                round_hints_session_score.update_print_round_hints(
                    hint_choice2,
                    round_card[f"{hint_choice2}"],
                )
            break
        else:
            print(f"Please type '{hint_choice1}' or '{hint_choice2}'." + "\n")


