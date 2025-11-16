from turtle import Turtle, Screen

class Snake:

    def __init__(self):
        self.snake =[]
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[len(self.snake) - 1]

    def create_square(self):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        return timmy

    def extend(self):

        timmy = self.create_square()
        new_x = self.tail.xcor()
        new_y = self.tail.ycor()
        timmy.goto(x = new_x, y = new_y)
        self.snake.append(timmy)

    def create_snake(self):
        for i in range(3):
            timmy = self.create_square()
            timmy.goto(x=-20 * i, y=0)
            self.snake.append(timmy)


    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def reset(self):
        for part in self.snake:
            part.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]