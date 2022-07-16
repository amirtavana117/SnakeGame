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
        snake.Extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset_scoreBoard()
        snake.reset_snake()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score_board.reset_scoreBoard()
            snake.reset_snake()
screen.exitonclick()
