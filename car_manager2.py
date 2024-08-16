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
        self.create_car()
        self.cars_at_end = 0
        self.car_count = 0
        self.timer = 0
        self.last_spawn_time = 0

    def create_car(self):
        for i in range(5):
            car = Turtle()
            car.penup()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2)
            car.setpos(x=320, y=random.choice(STARTING_POSITIONS))
            self.cars.append(car)
            self.last_spawn_time = time.time()

    def create_cars(self):
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

    def create_cars_2(self):
        time_now = time.time()
        print(f'last spawn {time_now}')
        print(f'current spawn {time_now}')
        if time_now >= self.last_spawn_time + 1:
            if self.car_count < 60:
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
                self.last_spawn_time = time.time()
                return
        return
    
    def move_cars(self):
        for car in range(0, self.car_count):
            if self.cars[car].xcor() > -280:
                random_move = random.randint(2, 15)
                self.cars[car].goto(y=self.cars[car].ycor(), x=self.cars[car].xcor() - random_move * 0.3)
            else:
                self.cars_at_end += 1
                random_position = random.choice(STARTING_POSITIONS)
                self.cars[car].setpos(x=280, y=random_position)
        self.create_cars_2()
        return







