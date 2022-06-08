from turtle import Turtle, Screen

positions = [(0, 0), (-20, 0), (-40, 0)]

# Initialized Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


segments = []
for seg in positions:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(seg)

screen.exitonclick()
