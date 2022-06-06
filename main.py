import time
import turtle
from turtle import Screen
from snake import Snake
from Food import Food
from Score import Score


def x_wall_collision():
    if snake.head.xcor() >= 384 or snake.head.xcor() <= -384:
        return True


def y_wall_collision():
    if snake.head.ycor() >= 288 or snake.head.ycor() <= -288:
        return True


def game_over():
    if x_wall_collision():
        return True
    elif y_wall_collision():
        return True
    for turt in snake.turtles[:-2]:  # collision with self
        if snake.head.distance(turt) < 10:
            return True


turtle.colormode(255)
screen = Screen()
screen.title("Snake Game")
screen.bgcolor(0, 0, 0)
screen.setup(width=800, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score(0, 280)

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

speed = screen.textinput("Game speed selection", "Choose between normal and fast speeds.")
if speed.lower() == 'fast':
    speed = 0.05
else:
    speed = 0.075
screen.listen()

while True:
    if game_over():
        screen.textinput(title='Game Over', prompt=f'Your final score is {score.get_score()}.\nEnter any key to exit.')
        break

    if food.distance(snake.head) < 15:  # Eating food
        food.refresh()
        snake.grow()
        score.increase_score()
    snake.move()
    time.sleep(speed)
    screen.update()
