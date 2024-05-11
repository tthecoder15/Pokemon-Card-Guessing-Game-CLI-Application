import os
from game_dialogue import gameplay_dialogue
from random_card_gen import gen_rand_card
from game_loops import hint_guess_loop, choose_hint_loop, guess_loop


def standard_game(scoreboard, session_hints_score):
    round_card = gen_rand_card("standard")
    # Card for round generated
    os.system("clear")
    session_hints_score.update_hints("hint_1", round_card["flavor_text"])
    # First hint, flavor text added to hints list
    session_hints_score.hint_reminder()
    # Hints list (only flavour text so far), printed to terminal
    hint_guess_loop(round_card, session_hints_score, scoreboard, "guess_or_hint1")
    # Player offered guess or hint ^
    choose_hint_loop(
        round_card,
        session_hints_score,
        "2nd_hint_prompt",
        "retreat",
        "attack",
    )
    # Player prompted to choose which hint ^
    session_hints_score.hint_reminder()
    # Player's current hints printed ^
    hint_guess_loop(round_card, session_hints_score, scoreboard, "guess_or_hint2")
    # Player offered guess or hint ^
    choose_hint_loop(
        round_card,
        session_hints_score,
        "3rd_hint_prompt",
        "stage",
        "type",
    )
    # Player prompted to choose which hint
    session_hints_score.hint_reminder()
    # Player's current hints printed
    print(gameplay_dialogue["mandatory_guess"])
    # Player prompted to guess
    guess_loop(round_card, session_hints_score, scoreboard)
    # Guess initiated


def hard_game(scoreboard, session_hints_score):
    session_hints_score.hint_reset()
    # Hints reset
    round_card = gen_rand_card("hard")
    # Card for round generated
    os.system("clear")
    session_hints_score.update_hints("hint_1", round_card["flavor_text"])
    # First hint, flavor text added to hints list
    session_hints_score.hint_reminder()
    # Hints list (only flavor text so far), printed to terminal
    hint_guess_loop(round_card, session_hints_score, scoreboard, "guess_or_hint1")
    # Player offered guess or hint ^
    choose_hint_loop(
        round_card,
        session_hints_score,
        "2nd_hint_hard",
        "stage",
        "attack",
    )
    # Player prompted to choose which hint between attack and stage
    session_hints_score.hint_reminder()
    # Player's current hints printed ^
    session_hints_score.hint_reminder()
    # Player's current hints printed
    print(gameplay_dialogue["mandatory_guess_hard"])
    # Player prompted to guess
    guess_loop(round_card, session_hints_score, scoreboard)
    # Guess initiated
