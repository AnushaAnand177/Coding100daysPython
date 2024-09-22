from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        """
        Initializes the scoreboard object.

        Sets up initial scoreboard state with the following:
        - A score initialized to zero.
        - The color set to white for rendering text.
        - Pen in the up position to avoid drawing lines when moving.
        - Turtle hidden from view.
        - Turtle positioned at coordinates (0, 260) on the screen.
        - Updates the scoreboard with the initial score.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        :return: None. Updates the scoreboard with the current score by writing it to the display.
        """
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        """
        Displays a "GAME OVER" message at the center of the screen.

        :return: None
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """
        Increases the player's score by 1, then clears and updates the scoreboard.

        :return: None
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()