from abc import update_abstractmethods
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.goto(0, 255)
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} , high score : {self.highscore}", align="center",
                   font=("Arial", 24, "normal"))

    def reset_scoreBoard(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def inceraseScore(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
