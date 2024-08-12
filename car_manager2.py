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
        self.cars_at_end = 0
        self.car_count = 6

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
        if self.car_count < 70:
            self.car_count += 1
            print(f'cars total {self.car_count}')
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
        # print(end_range)
        for car in range(0, self.car_count):
            print(f'iterator :{car}, actual list length: {len(self.cars)}')
            # print(f'3 : {len(self.cars)}')
            # print(self.cars[car].xcor())
            # self.delete_car(car)
            if self.cars[car].xcor() > -280:
                random_move = random.randint(2, 15)
                self.cars[car].goto(y=self.cars[car].ycor(), x=self.cars[car].xcor() - random_move)
            else:
                print(f'car reached xcor : {self.cars[car].xcor()}')

                self.cars_at_end += 1
                # del self.cars[car]
                # self.car_count -= 1
                self.cars[car].setpos(x=280, y=self.cars[car].ycor())
                # del self.cars[car]
                # self.car_count -= 1
                # self.delete_car(self.cars[car])
                # print(f'car count : {self.car_count}')

        self.create_car()
        return






