from turtle import Turtle, Screen

class Paddle:

    def __init__(self, side):
        self.paddle = self.create_paddle(side)


    def create_paddle(self,side):
        timmy = Turtle(shape="square")
        timmy.penup()
        timmy.hideturtle()
        timmy.color("white")
        timmy.shapesize(stretch_wid=5, stretch_len=1)
        if side == "left":
            timmy.goto(x= -350, y= 0)
        else:
            timmy.goto(x= 350, y= 0)
        timmy.showturtle()
        return timmy



    def up(self):
        if self.paddle.ycor() < 240:
            new_y = self.paddle.ycor() + 20
            self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        if self.paddle.ycor() > -240:
            new_y = self.paddle.ycor() - 20
            self.paddle.goto(self.paddle.xcor(), new_y)

