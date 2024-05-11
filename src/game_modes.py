import os
from game_dialogue import standard_dialogue
from random_card_gen import gen_rand_card
from game_loops import hint_guess_loop, choose_hint_loop, guess_loop


def standard_game(scoreboard, round_hints_session_score):
    round_hints_session_score.hint_reset()
    # Hints reset
    round_card = gen_rand_card()
    # Card for round generated

    os.system("clear")

    round_hints_session_score.update_hints("hint_1", round_card["flavor_text"])
    # First Hint, flavor text ^

    round_hints_session_score.hint_reminder()

    hint_guess_loop(round_card, round_hints_session_score, scoreboard, "guess_or_hint1")

    # Player offered guess or hint ^

    choose_hint_loop(
        round_card,
        round_hints_session_score,
        "2nd_hint_prompt",
        "retreat",
        "attack",
    )
    # Player prompted to choose which hint ^

    round_hints_session_score.hint_reminder()
    # Player's current hints printed ^

    hint_guess_loop(round_card, round_hints_session_score, scoreboard, "guess_or_hint2")
    # Player offered guess or hint ^

    choose_hint_loop(
        round_card,
        round_hints_session_score,
        "3rd_hint_prompt",
        "stage",
        "type",
    )
    # Player prompted to choose which hint

    round_hints_session_score.hint_reminder()
    # Player's current hints printed

    print(standard_dialogue["mandatory_guess"])
    # Player prompted to guess

    guess_loop(round_card, round_hints_session_score, scoreboard)
    # Guess initiated

def hard_game(scoreboard, round_hints_session_score):
    round_hints_session_score.hint_reset()
    # Hints reset
    round_card = gen_rand_card()
    # Card for round generated

    os.system("clear")

    round_hints_session_score.update_hints("hint_1", round_card["flavor_text"])
    # First Hint, flavor text ^

    round_hints_session_score.hint_reminder()

    hint_guess_loop(round_card, round_hints_session_score, scoreboard, "guess_or_hint1")

    # Player offered guess or hint ^

    choose_hint_loop(
        round_card,
        round_hints_session_score,
        "2nd_hint_prompt",
        "retreat",
        "attack",
    )
    # Player prompted to choose which hint ^

    round_hints_session_score.hint_reminder()
    # Player's current hints printed ^

    hint_guess_loop(round_card, round_hints_session_score, scoreboard, "guess_or_hint2")
    # Player offered guess or hint ^

    choose_hint_loop(
        round_card,
        round_hints_session_score,
        "3rd_hint_prompt",
        "stage",
        "type",
    )
    # Player prompted to choose which hint

    round_hints_session_score.hint_reminder()
    # Player's current hints printed

    print(standard_dialogue["mandatory_guess"])
    # Player prompted to guess

    guess_loop(round_card, round_hints_session_score, scoreboard)
    # Guess initiated

