from Food import Food
from ScoreBoard import ScoreBoard
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
food = Food()
score_board = ScoreBoard()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

Game_Is_on = True

while Game_Is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.Refresh()
        score_board.inceraseScore()


screen.exitonclick()
