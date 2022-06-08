from turtle import Turtle, Screen
import time
positions = [(0, 0), (-20, 0), (-40, 0)]

# Initialized Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create Snake
segments = []
for seg in positions:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(seg)
    segments.append(segment)


Game_Is_on = True

while Game_Is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments)-1, 0, -1):
        new_x = segments[seg-1].xcor()
        new_y = segments[seg-1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)
screen.exitonclick()
