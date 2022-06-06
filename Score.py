from turtle import Turtle

ALIGNMENT = "center"
FONT =('Montserrat', 10, 'bold')


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(x, y)
        self.write("Score: 0", align="center", font=('Montserrat', 10, 'bold'))
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def get_score(self):
        return self.score


