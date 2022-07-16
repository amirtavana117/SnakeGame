from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 10005)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.segments[0].heading() != 90:
            self.head.setheading(270)

    def Extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
