from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x= -250, y= 250)
        self.write_score()

    def increase_level(self):
        self.level += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))