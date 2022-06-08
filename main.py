from Snake import Snake
from turtle import Screen
import time


# Initialized Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()


Game_Is_on = True

while Game_Is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()
