import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITIONS = [-240, -220, -200, -140, -80, -40, 0, 60, 90, 120, 160, 210, 230, 260]


class CarManager:

    def __init__(self):
        self.cars = []

        self.create_cars()
        self.cars_at_end = 0
        self.car_count = 0

    def create_cars(self):
        car = Turtle()
        car.penup()
        car.shape('square')
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2)
        car.setpos(x=320, y=random.choice(STARTING_POSITIONS))
        car.setheading(180)
        self.cars.append(car)
        # for color in COLORS:
        #     car = Turtle()
        #     car.penup()
        #     car.shape('square')
        #     car.color(color)
        #     car.shapesize(stretch_len=2)
        #     car.setpos(x=320, y=random.choice(STARTING_POSITIONS))
        #     car.setheading(180)
        #     self.cars.append(car)

    def create_car(self):
        timer = 0
        if self.car_count < 60:
            # while timer != 1:
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
            timer += 0.01


    # def check_space(self):
    #     for car in self.cars:
    #         if car
    #     if self.car_count < 10:
    #         return True
    #     else:
    #         return False

    def move_cars(self):
        end_range = len(self.cars)
        # print(end_range)

        for car in range(0, self.car_count):
            print(self.cars[car].xcor())
            if self.cars[car].xcor() > -280:
                random_move = random.randint(2, 15)
                self.cars[car].goto(y=self.cars[car].ycor(), x=self.cars[car].xcor() - random_move * 0.3)

            else:
                print(f'car reached xcor : {self.cars[car].xcor()}')

                self.cars_at_end += 1

                # self.cars[car].setpos(x=280, y=self.cars[car].ycor())  # to select a new random y cor
                random_position = random.choice(STARTING_POSITIONS)
                self.cars[car].setpos(x=280, y=random_position)
        # print(self.cars[1].xcor())
        self.create_car()
        return






