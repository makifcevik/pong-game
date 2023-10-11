from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)

        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_left(self):
        self.l_score += 1
        self.update()

    def increase_right(self):
        self.r_score += 1
        self.update()
