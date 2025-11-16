from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_clockwise():
    timmy.right(5)

def turn_counter_clockwise():
    timmy.left(5)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key = "w",fun=move_forwards)
screen.onkey(key = "s",fun=move_backwards)
screen.onkey(key = "d",fun=turn_clockwise)
screen.onkey(key = "a",fun=turn_counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

