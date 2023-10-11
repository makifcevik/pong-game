from turtle import Turtle

MULTIPLIER = 1.05  # to make the ball speed up on bounce
SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("white")

        self.direction = 35
        self.move_speed = SPEED

    def move(self):
        self.setheading(self.direction)
        self.forward(self.move_speed)
        self.bounce_y()

    def bounce_y(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.direction = 360 - self.heading()
            self.increase_speed()

    def bounce_x(self):
        self.direction = 180 - self.heading()
        self.increase_speed()

    def restart(self):
        self.goto(0, 0)
        self.direction = 180 - self.direction
        self.move_speed = SPEED

    def increase_speed(self):
        self.move_speed = self.move_speed * MULTIPLIER
