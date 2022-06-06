from turtle import Turtle

FIRST_TURTLE = -1

LS = ["red", "white", "orange"]
SIZE = 0.8
MOVE_DISTANCE = 16
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = [Turtle(shape='square') for i in range(3)]
        self.create_snake()
        self.head = self.turtles[-1]

    def create_snake(self):
        position = (0, 0)
        for turt in self.turtles:
            turt.penup()
            [tur.shapesize(SIZE, SIZE) for tur in self.turtles]
            turt.goto(position)
            turt.color("white")
            position = list(position)
            position[0] += MOVE_DISTANCE
            position = tuple(position)

    def move(self):
        for i in range(len(self.turtles) - 1):
            new_coordinates = self.turtles[i + 1].pos()
            self.turtles[i].goto(new_coordinates)
        self.head.forward(MOVE_DISTANCE)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def grow(self):
        tom: Turtle = Turtle(shape="square")
        tom.shapesize(SIZE, SIZE)
        tom.penup()
        tom.color("white")
        self.turtles.insert(0, tom)
