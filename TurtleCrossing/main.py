import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    #Detect player reaching finish
    if player.is_finished():
        player.restart()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()