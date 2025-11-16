from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x= 0, y= 270)
        self.write(f"{self.score_left} : {self.score_right}", align= "center", font= ("Courier", 20, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"{self.score_left} : {self.score_right}", align="center", font=("Courier", 20, "normal"))

    def right_scored(self):
        self.score_right += 1

    def left_scored(self):
        self.score_left += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 20, "normal"))