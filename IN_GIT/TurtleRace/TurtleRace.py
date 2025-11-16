import random
import turtle
from turtle import Turtle, Screen


race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color")
turtles = []
colors = ["blue", "red","green", "yellow", "purple"]


for i in range(0,5):
    timmy = Turtle(shape='turtle')
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(-230,100 - 50*i)
    turtles.append(timmy)


if user_bet:
    race_on = True

while(race_on):
    for i in range(0,5):

        if turtles[i].xcor() > 230:
            race_on = False
            winner = turtles[i].pencolor()
            if winner == user_bet:
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner!")
        rand_dist = random.randint(0, 10)
        turtles[i].forward(rand_dist)

screen.exitonclick()


