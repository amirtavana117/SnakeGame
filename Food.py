from tkinter import S
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("Red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        random_x = random.randint(-225, 225)
        random_y = random.randint(-225, 255)
        self.goto(random_x, random_y)

    def Refresh(self):
        random_x = random.randint(-225, 225)
        random_y = random.randint(-225, 255)
        self.goto(random_x, random_y)
