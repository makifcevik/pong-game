from turtle import Turtle

SPEED = 50


class Paddle(Turtle):

    def __init__(self, pos: tuple):
        super().__init__()
        self.start_position = pos
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto(pos)

    def move_up(self):
        self.sety(self.ycor() + SPEED)
        if self.ycor() > 240:
            self.sety(240)

    def move_down(self):
        self.sety(self.ycor() - SPEED)
        if self.ycor() < -230:
            self.sety(-230)

    def restart(self):
        self.goto(self.start_position)
