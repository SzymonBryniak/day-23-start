import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITIONS = [-240, -200, -140, -80, -40, 0, 60, 90, 120, 160, 210, 260]


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for color in COLORS:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.color(color)
            car.shapesize(stretch_len=2)
            car.setpos(x=320, y=STARTING_POSITIONS[COLORS.index(color)])
            car.setheading(180)
            self.cars.append(car)

    def create_car(self):
        random_color = random.randint(0, len(COLORS)-1)
        random_position = random.randint(0, len(STARTING_POSITIONS)-1)
        car = Turtle()
        car.penup()
        car.shape('square')
        car.color(COLORS[random_color])
        car.shapesize(stretch_len=2)
        car.setpos(x=320, y=STARTING_POSITIONS[random_position])
        self.cars.append(car)

    def check_space(self):

        pass

    def move_cars(self):
        end_range = len(self.cars)
        print(end_range)
        for car in range(0, len(self.cars)):
            print(f'3 : {len(self.cars)}')
            print(self.cars[car].xcor())
            # self.delete_car(car)
            if self.cars[car].xcor() > -280:
                random_move = random.randint(2, 15)
                self.cars[car].goto(y=self.cars[car].ycor(), x=self.cars[car].xcor() - random_move)
            # else:
                # self.cars[car].setpos(x=280, y=self.cars[car].ycor())

        return self.create_car()

    def delete_car(self, car):
        # for car in range(0, len(self.cars)):
        print(f'from move cats iterator : {car}')
        if self.cars[car].xcor() <= -290:
            self.cars.pop(car)
            print(f'len : {len(self.cars)}')

    # def add_car(self, number_of_cars):
    #     self.create_car()
    #     random_value = random.randint(0, 5)
    #     random_postion = STARTING_POSITIONS[random_value]
    #     starting_position = 0
    #     cars = len(self.cars)
    #     for car in range(0 , cars):
    #         if player.distance(cars.cars[i]) < 25 and player.xcor():
    #             continue
    #
    #     if self.cars[-1].xcor < 260:
    #         car = Turtle()
    #         car.penup()
    #         car.shape('square')
    #         car.color(COLORS[random_value])
    #         car.shapesize(stretch_len=2)
    #         car.setpos(x=320, y=starting_position)
    #           # I will spawn additional cars in predefined positions excluding the position of the last car or in the position of the last car if the
    #         # xcor of the last car is beyond a predefined minimum coordinate away from the spawn of the new car.
    #     return





