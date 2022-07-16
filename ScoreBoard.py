from abc import update_abstractmethods
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = self.ReadFile()
        self.goto(0, 255)
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def ReadFile(self):
        with open("score.txt") as file:
            score_ = int(file.read())
        return score_

    def Write_file(self, score):
        with open("score.txt", 'w') as file:
            file.write(str(score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} , high score : {self.highscore}", align="center",
                   font=("Arial", 24, "normal"))

    def reset_scoreBoard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.Write_file(self.score)
        self.score = 0
        self.update_scoreboard()

    def inceraseScore(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
