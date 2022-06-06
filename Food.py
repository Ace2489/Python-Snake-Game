import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.6, 0.6)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-370, 370)
        y = random.randint(-280, 280)
        self.goto(x, y)
