from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.hideturtle()
        self.penup()
        self.color("black")
        self.restart()
        self.setheading(90)
        self.showturtle()
        self.finished = False

    def move(self):
        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE*5)

    def restart(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() > 270:
            return True
        else:
            return False
