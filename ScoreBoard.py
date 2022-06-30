from abc import update_abstractmethods
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 255)
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=("Arial", 24, "normal"), align="center")

    def inceraseScore(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
