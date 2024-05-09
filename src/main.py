import os
from standard_game import standard_game
from game_dialogue import menu_dialogue
from hints_and_score import HintsAndScore
from game_loops import Quit, PlayAgain

class Exit(Exception):
    pass

def hard_mode_game():
    print("This will trigger the hard mode of the game")
    raise Exception("Hard mode function not yet defined")


def scoreboard():
    print("This will trigger the scoreboard functionality")
    raise Exception("Scoreboard functionality not defined yet")


def menu():
    while True:
        os.system("clear")
        print(menu_dialogue["greeting"])

        try: 
            while True:
                response = input()
                if response.lower() == "scoreboard" or response.lower() == "'scoreboard'":
                    # Need to return scoreboard here
                    scoreboard()
                if response.lower() == "exit" or response.lower() == "'exit'":
                    # Need to return scoreboard here
                    raise Exit
                else:
                    break
        except Exit:
            print("Goodbye!")
            break

        os.system("clear")
        print(menu_dialogue["mode_choice"])

        try: 
            while True:
                session_hints_score = HintsAndScore()
                response = input()

                if response.lower() == "hard" or response.lower() == "'hard'":
                    # Need to run hardmode here
                    hard_mode_game()

                else:
                    while True:
                        try:
                            session_hints_score.hint_reset()
                            standard_game(session_hints_score)
                        except PlayAgain:
                            pass
        except Quit:
            pass


menu()
