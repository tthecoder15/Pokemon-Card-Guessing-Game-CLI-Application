"""Contains class used to track hints and user score.
"""

from game_dialogue import hint_dialogue

class HintsAndScore:
    """Class that tracks and contains methods relating to user score and hints.
    """    
    def __init__(self):
        self.hints = []
        self.streak = 0
        self.score = 0

    def update_hints(self, dialogue_key, card_data):
        """Updates the HintsAndScore instance hints attribute and stores hint data.

        Parameters
        ----------
        dialogue_key : _dict key value_
            A dictonary key value corresponding to which hint the user would be selecting.
        card_data : _str_
            The hint string from the mystery card dict.
        """        
        hint_string = (
            hint_dialogue[f"{dialogue_key}"] + "\n" + '"' + card_data + '"' + "\n"
        )
        self.hints.append(hint_string)

    def hint_reminder(self):
        """Prints all hints currently stored.
        """
        for hint in self.hints:
            print(hint)

    def hint_reset(self):
        """Resets stored hints. 
        """        
        self.hints = []

    def update_score(self):
        """Updates session score using the number of hints received.
        """        
        if self.score < 0:
            # Accounts for scoring errors where score is less than zero
            print("FOR SOME REASON THE SCORE WAS LESS THAN 0")
            self.score = 0

        num_of_hints = len(self.hints)
        self.score += int(
            (12 - num_of_hints ^ 2 - num_of_hints) * (1 + 1 * (self.streak / 10))
        )
        self.streak += 1

    def reset_streak_score(self):
        """Resets session score and streak values.
        """        
        self.score = 0
        self.streak = 0

    def get_score(self):
        """Returns session score.

        Returns
        -------
        _int_
            The session score.
        """        
        return self.score

    def get_streak(self):
        """Returns session streak.

        Returns
        -------
        _int_
            The session streak of correct answers.
        """        
        return self.streak

    def streak_and_score(self, correct):
        """Returns a string reacting to guess assessment that contains session streak and score.

        Parameters
        ----------
        correct : _bool_
            Describes if the user guessed correctly or incorrectly.
        """        
        if correct is True:
            print(f"\nGreat work! Your current score is: \n{self.get_score()}.")
            print(f"Your current streak is: \n{self.get_streak()}.")
        if correct is False:
            print(f"Tough luck! Your session score was: \n{self.get_score()}.")
            print(f"\nYour session streak was: {self.get_streak()}.")
