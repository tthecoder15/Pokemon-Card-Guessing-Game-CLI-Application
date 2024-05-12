import json
from numpy import random
from game_dialogue import scoreboard_dialogue
from game_loops import Menu
import os


class ScoreAdded(Exception):
    pass


class SameScore(Exception):
    pass


class Scoreboard:
    """
    Used to initialise a scoreboard object for reading/writing in the different modes.
    """

    def __init__(self):
        self.active_sb = []
        self.active_gamemode = ""
        self.session_score_id = 0

    def set_current_game_mode(self, game_mode):
        # Initialises local copy of scoreboard variable based on what mode is loaded, generates a session ID that is used to ensure scores are not copied twice if the player plays multiple times
        if game_mode == "standard":
            self.active_gamemode = game_mode
            with open("scoreboards/standard_scoreboard.json") as f:
                self.active_sb = json.load(f)
        elif game_mode == "hard":
            self.active_gamemode = game_mode
            with open("scoreboards/hard_scoreboard.json") as f:
                self.active_sb = json.load(f)
        else:
            raise ValueError("Please pass a game mode")
        while True:
            gen_score_id = random.randint(0, 9999)
            duplicate_id = False
            for score in self.active_sb:
                if score["session_score_id"] == gen_score_id:
                    duplicate_id = True
            if duplicate_id is False:
                self.session_score_id = gen_score_id
                break

    def check(self):
        print("This is the active scoreboard value:", self.active_sb)

    # This needs formatting later ^

    def name_entry_loop(self):
        print("Please enter a name for your high score! (Max five characters): ")
        while True:
            score_name = input()
            if len(score_name) <= 5:
                break
            print(f"You entered: '{score_name}'.")
            print("Please enter a name that is five or less characters.")
        return score_name

    def update(self, session_score):
        if session_score <= 0:
            # Immediately checks if sessions score is above 0 and if not, exits
            return
        is_same_session = False
        updated_old_score = {}
        try:
            for index, scoreboard_entry in enumerate(self.active_sb):
                if scoreboard_entry["session_score_id"] == self.session_score_id:
                    is_same_session = True
                    if scoreboard_entry["score"] == session_score:
                        raise SameScore
                    updated_old_score = self.active_sb.pop(index)
                    updated_old_score["score"] = session_score
        except SameScore:
            return
        try:
            for index, scoreboard_entry in enumerate(self.active_sb):
                if session_score > scoreboard_entry["score"]:
                    if is_same_session is True:
                        self.active_sb.insert(index, updated_old_score)
                        raise ScoreAdded
                    else:
                        score_name = self.name_entry_loop()
                        self.active_sb.insert(
                            index,
                            {
                                "name": score_name,
                                "session_score_id": self.session_score_id,
                                "score": session_score,
                            },
                        )
                    raise ScoreAdded
                elif (
                    session_score == scoreboard_entry["score"]
                    and is_same_session is True
                ):
                    self.active_sb.append(updated_old_score)
                    raise ScoreAdded
            if len(self.active_sb) < 5 and is_same_session is False:
                score_name = self.name_entry_loop()
                self.active_sb.append(
                    {
                        "name": score_name,
                        "session_score_id": self.session_score_id,
                        "score": session_score,
                    },
                )
        except ScoreAdded:
            pass

        if len(self.active_sb) > 5:
            self.active_sb.pop()

        if self.active_gamemode == "standard":
            with open("scoreboards/standard_scoreboard.json", "w") as f:
                json.dump(self.active_sb, f)
        elif self.active_gamemode == "hard":
            with open("scoreboards/hard_scoreboard.json", "w") as f:
                json.dump(self.active_sb, f)


def scoreboard_viewer():
    os.system("clear")
    while True:
        print(scoreboard_dialogue["which_scoreboard"])
        while True:
            response = input().lower()
            if response == "standard" or response == "'standard'":
                with open("scoreboards/standard_scoreboard.json") as f:
                    loaded_sb = json.load(f)
                print(scoreboard_dialogue["standard_sb_print"])
                for index, entry in enumerate(loaded_sb):
                    print(f"{index+1}. Name: {entry['name']}, Score: {entry['score']}")
                print()
                break
            elif response == "hard" or response == "'hard'":
                with open("scoreboards/hard_scoreboard.json") as f:
                    loaded_sb = json.load(f)
                print(scoreboard_dialogue["hard_sb_print"])
                for index, entry in enumerate(loaded_sb):
                    print(f"{index+1}. Name: {entry['name']}, Score: {entry['score']}")
                print()
                break
            elif response == "menu" or response == "'menu'":
                raise Menu
            else:
                print(scoreboard_dialogue["which_sb_loop"])
