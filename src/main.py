"""The instigating function that is run to play the "Guess that Pokémon" game.

Uses a loop as a menu to navigate to gameplay mode selection or to view the scoreboard.
Within game mode branch, a makes the user choose between playing again or quitting.

Raises
------
Exception
    _description_
Exception
    _description_
Exit
    Used to terminate the app.
"""

import os
from game_modes import standard_game, hard_game
from game_dialogue import menu_dialogue
from hints_and_score import HintsAndScore
from game_loops import Menu, PlayAgain
from scoreboard import Scoreboard, scoreboard_viewer


class Quit(Exception):
    pass


def menu():
    while True:
        os.system("clear")
        try:
            while True:
                print(menu_dialogue["greeting"])
                response = input().lower()
                if response == "scoreboard" or response == "'scoreboard'":
                    try:
                        scoreboard_viewer()
                    except Menu:
                        os.system("clear")
                elif response == "play" or response == "'play":
                    break
                elif response == "quit" or response == "'quit'":
                    raise Quit
                else:
                    print(menu_dialogue["greeting_loop"])
        except Quit:
            print("Goodbye!")
            break

        os.system("clear")
        print(menu_dialogue["mode_choice"])

        try:
            while True:
                session_hints_score = HintsAndScore()
                scoreboard = Scoreboard()
                response = input()

                if response.lower() == "hard" or response.lower() == "'hard'":
                    scoreboard.set_current_game_mode("hard")
                    while True:
                        try:
                            session_hints_score.hint_reset()
                            os.system("clear")
                            hard_game(scoreboard, session_hints_score)
                        except PlayAgain:
                            pass

                else:
                    scoreboard.set_current_game_mode("standard")
                    while True:
                        try:
                            session_hints_score.hint_reset()
                            os.system("clear")
                            standard_game(scoreboard, session_hints_score)
                        except PlayAgain:
                            pass
        except Menu:
            pass


menu()
