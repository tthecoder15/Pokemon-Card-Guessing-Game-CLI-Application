import json
from numpy import random


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

    def update(self, session_score):
        if session_score < 0:
            # Immediately checks if sessions score is above 0 and if not, exits
            return
        same_session = False
        for index, score in enumerate(self.active_sb):
            if score["session_score_id"] == self.session_score_id:
                same_session = self.active_sb.pop(index)
                same_session["score"] = session_score
        # Checks if any of the scores in the scoreboard are the active one based on session id, if it is the same, the original score is removed from the list and copied to a local var for addition to the list later

        for index, score in enumerate(self.active_sb):
            # Cycles through scores in scoreboard and enumerates to keep track of their index position
            if score["score"] < session_score:
                # If the session score is greater than any scoreboard value, process begins to save it
                if bool(same_session):
                    self.active_sb.insert(index, same_session)
                    break
                # If same session, score is inserted in the scoreboard list without requiring a new name entry and loop is broken
                else:
                    # If not the same session, user is prompted to input a name to save with their record, loop doesn't end until user follows name convention
                    print(
                        "Please enter a name for your high score! (Max five characters): "
                    )
                    while True:
                        score_name = input()
                        if len(score_name) <= 5:
                            self.active_sb.insert(
                                index,
                                {
                                    "name": score_name,
                                    "session_score_id": self.session_score_id,
                                    "score": session_score,
                                },
                            )
                            break
                        else:
                            print(
                                f"You entered: '{score_name}'. Please enter a name that is five or less characters."
                            )
        if len(self.active_sb) < 5 and same_session is False:
            print("Please enter a name for your high score! (Max five characters): ")
            while True:
                score_name = input()
                if len(score_name) <= 5:
                    self.active_sb.append(
                        {
                            "name": score_name,
                            "session_score_id": self.session_score_id,
                            "score": session_score,
                        }
                    )
                    break
                else:
                    print(
                        f"You entered: '{score_name}'. Please enter a name that is five or less characters."
                    )
        if len(self.active_sb) > 5:
            self.active_sb.pop()
        # Below assess which game mode is active, open that JSON file and overwrite it with the new scoreboard list of dicts
        if self.active_gamemode == "standard":
            with open("scoreboards/standard_scoreboard.json", "w") as f:
                json.dump(self.active_sb, f)
        elif self.active_gamemode == "hard":
            with open("scoreboards/hard_scoreboard.json", "w") as f:
                json.dump(self.active_sb, f)
