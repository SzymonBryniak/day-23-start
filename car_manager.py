from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITIONS = [-240, -140, -40, 60, 160, 260]


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
            car.setpos(x=280, y=STARTING_POSITIONS[COLORS.index(color)])
            car.setheading(180)
            self.cars.append(car)

    def move_cars(self):
        for car in COLORS:
            if self.cars[COLORS.index(car)].xcor() > - 280:
                random_move = random.randint(2, 8)
                # self.cars[COLORS.index(car)].forward(10 * random_move)
                self.cars[COLORS.index(car)].goto(y=STARTING_POSITIONS[COLORS.index(car)], x=self.cars[COLORS.index(car)].xcor() - random_move)
            else:
                self.cars[COLORS.index(car)].setpos(x=280, y=STARTING_POSITIONS[COLORS.index(car)])
        return

    def cars_reset(self):
        pass




