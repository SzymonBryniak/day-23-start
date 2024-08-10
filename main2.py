import time
from turtle import Screen
from player import Player
from car_manager2 import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard.display_score()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkeypress(player.go_up, key='Up')
    time.sleep(0.1)
    screen.update()
    cars.move_cars()
    for i in range(0, 6):  # to adjust range to cover additional cars
        if player.distance(cars.cars[i]) < 25 and player.xcor():
            print('game over')
            scoreboard.update_score(-1)
            game_is_on = False
            gm_prompt = screen.textinput('game over', 'Enter "Yes" to play again ')
            if gm_prompt == 'Yes':
                player.reset_player()
                game_is_on = True
        if player.ycor() > 270:
            print('you win')
            scoreboard.update_score(1)
            gm_prompt = screen.textinput('you win', 'Enter "Yes" to play again ')
            if gm_prompt == 'Yes':
                player.reset_player()
                game_is_on = True

screen.exitonclick()

