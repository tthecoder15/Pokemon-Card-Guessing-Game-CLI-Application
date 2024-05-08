import os
from guess import guess
from game_dialogue import standard_dialogue, hint_dialogue
from random_card_gen import gen_rand_card
from hints_and_score import HintsAndScore
from game_loops import hint_guess_loop, choose_hint_loop


def standard_game():
    session_hints_and_score = HintsAndScore()
    # HintsAndScore instance initiated
    round_card = gen_rand_card()
    # Card for round generated

    os.system("clear")
    session_hints_and_score.update_hints(
        "hint_1", round_card["flavor_text"]
    )
    # First Hint, flavor text ^

    session_hints_and_score.hint_reminder()

    hint_guess_loop(
        round_card, session_hints_and_score, "guess_or_hint1"
    )
    # Player offered guess or hint ^

    choose_hint_loop(
        round_card,
        session_hints_and_score,
        "2nd_hint_prompt",
        "retreat",
        "attack",
    )
    # Player prompted to choose which hint ^

    session_hints_and_score.hint_reminder()
    # Player's current hints printed ^

    hint_guess_loop(
        round_card, session_hints_and_score, "guess_or_hint2"
    )
    # Player offered guess or hint ^

    choose_hint_loop(
        round_card,
        session_hints_and_score,
        "3rd_hint_prompt",
        "stage",
        "type",
    )
    # Player prompted to choose which hint

    session_hints_and_score.hint_reminder()
    # Player's current hints printed

    print(standard_dialogue["mandatory_guess"])
    # Player prompted to guess

    guess(round_card, session_hints_and_score)
    # Guess initiated


# print(gen_rand_card())
# standard_game()
