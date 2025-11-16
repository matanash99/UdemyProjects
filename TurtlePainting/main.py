###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle

import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)


color_list = [(181, 9, 35), (210, 158, 95), (239, 214, 85), (182, 168, 15), (176, 77, 30), (215, 132, 160), (179, 15, 9), (127, 177, 200), (54, 95, 151), (31, 43, 69), (65, 23, 46), (164, 53, 81), (102, 188, 163), (221, 68, 115), (237, 68, 39), (60, 45, 109), (30, 138, 93), (77, 33, 23), (232, 205, 4), (40, 173, 149), (235, 164, 182), (147, 209, 220), (48, 168, 185), (234, 172, 161), (150, 217, 196), (166, 185, 226)]

timmy = Turtle()
timmy.ht()
timmy.setheading(225)
timmy.penup()
timmy.forward(170)
timmy.setheading(0)
timmy.st()

timmy.speed("fastest")
for j in range(10):

    for i in range(10):
        timmy.dot(10,random.choice(color_list))
        timmy.penup()
        timmy.forward(25)

    if j < 9:
        timmy.backward(250)
        timmy.left(90)
        timmy.forward(25)
        timmy.right(90)

timmy.ht()

screen = Screen()
screen.exitonclick()