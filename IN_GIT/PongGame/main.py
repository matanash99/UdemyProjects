from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Game objects
right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

# Key-hold flags
keys_held = {
    "Up": False,
    "Down": False,
    "w": False,
    "s": False
}

# Paddle keypress handlers
def key_press(key):
    keys_held[key] = True

def key_release(key):
    keys_held[key] = False

# Continuous paddle movement
def move_paddles():
    if keys_held["Up"]:
        right_paddle.up()
    if keys_held["Down"]:
        right_paddle.down()
    if keys_held["w"]:
        left_paddle.up()
    if keys_held["s"]:
        left_paddle.down()
    screen.ontimer(move_paddles, 20)

# Key bindings
screen.listen()
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Down"), "Down")
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("s"), "s")

# Start paddle movement loop
move_paddles()

# Game loop
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce off top and bottom
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce()

    # Paddle collisions
    if (ball.distance(right_paddle.paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(left_paddle.paddle) < 50 and ball.xcor() < -320):
        ball.hit_paddle()

    # Missed ball
    if ball.xcor() < -400:
        scoreboard.right_scored()
        scoreboard.update_score()
        ball.refresh()

    if ball.xcor() > 400:
        scoreboard.left_scored()
        scoreboard.update_score()
        ball.refresh()

screen.exitonclick()

