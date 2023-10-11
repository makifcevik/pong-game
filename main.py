from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

GAME_TICK = 0.03
GAME_START_DELAY = 1.5

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turns of the animation 

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

screen.update()
time.sleep(GAME_START_DELAY)


def reset_board():
    ball.restart()
    r_paddle.restart()
    l_paddle.restart()
    screen.update()
    time.sleep(GAME_START_DELAY)


is_game_on = True
while is_game_on:
    time.sleep(GAME_TICK)
    ball.move()

    # detect collision with the r_paddle
    if 320 <= ball.xcor() <= 350 and ball.distance(r_paddle) < 60:
        ball.bounce_x()

    # detect collision with the l_paddle
    if -350 <= ball.xcor() <= -320 and ball.distance(l_paddle) < 60:
        ball.bounce_x()

    # edge detection
    if ball.xcor() > 400:
        scoreboard.increase_left()
        reset_board()

    if ball.xcor() < -400:
        scoreboard.increase_right()
        reset_board()

    screen.update()

screen.exitonclick()
