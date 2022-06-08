from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for seg in POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(seg)
            self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_SPEED)
