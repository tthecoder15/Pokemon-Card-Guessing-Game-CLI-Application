from game_dialogue import hint_dialogue

class HintsAndScore:
    def __init__(self):
        self.hints = []
        self.streak = 0
        self.score = 0

    def update_hints(self, dialogue_key, card_data):
        hint_string = (
            hint_dialogue[f"{dialogue_key}"] + "\n" + '"' + card_data + '"' + "\n"
        )
        self.hints.append(hint_string)

    def hint_reminder(self):
        for hint in self.hints:
            print(hint)

    def hint_reset(self):
        self.hints = []

    def update_score(self):
        if self.score < 0:
            # Accounts for scoring errors where score is less than zero
            print("FOR SOME REASON THE SCORE WAS LESS THAN 0")
            self.score = 0

        num_of_hints = len(self.hints)
        self.score += int(
            (12 - num_of_hints ^ 2 - num_of_hints) * (1 + 1 * (self.streak / 10))
        )
        self.streak += 1

    def get_score(self):
        return self.score

    def get_streak(self):
        return self.streak

    def streak_and_score(self, correct):
        if correct is True:
            print(f"\nGreat work! Your current score is: \n{self.get_score()}.")
            print(f"Your current streak is: \n{self.get_streak()}.")
        if correct is False:
            print(f"Tough luck! Your session score was: \n{self.get_score()}.")
            print(f"\nYour session streak was: {self.get_streak()}.")
