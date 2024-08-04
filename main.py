import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()

screen.listen()
screen.onkeypress(player.go_up, key='Up')

screen.tracer(0)
game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    cars.move_cars()


screen.exitonclick()

