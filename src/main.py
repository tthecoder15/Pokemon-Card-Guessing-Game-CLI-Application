import os
from standard_game import standard_game
from game_dialogue import menu_dialogue
from hints_and_score import HintsAndScore
from guess import CorrectGuess, IncorrectGuess


def hard_mode_game():
    print("This will trigger the hard mode of the game")
    raise Exception("Hard mode function not yet defined")


def scoreboard():
    print("This will trigger the scoreboard functionality")
    raise Exception("Scoreboard functionality not defined yet")


def menu():
    os.system("clear")

    print(menu_dialogue["greeting"])
    while True:
        response = input()
        if response.lower() == "scoreboard" or response.lower() == "'scoreboard'":
            # Need to return scoreboard here
            scoreboard()

        else:
            break

    os.system("clear")
    print(menu_dialogue["mode_choice"])

    while True:
        session_hints_score = HintsAndScore()
        response = input()
        if response.lower() == "hard" or response.lower() == "'hard'":
            # Need to run hardmode here
            hard_mode_game()

        else:
            try:
                standard_game(session_hints_score)
            except CorrectGuess:
                print(
                    f"Great work! Your current score is: \n{session_hints_score.get_score()}. \nYour current streak is: {session_hints_score.get_streak()}."
                )
                print("So, would you like to play again?")
            except IncorrectGuess:
                pass


menu()
