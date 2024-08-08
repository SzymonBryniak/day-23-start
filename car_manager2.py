from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITIONS = [-240, -140, -40, 60, 160, 260]


class CarManager:

    def __init__(self):
        self.cars = []

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

    def create_random_car(self):
        random_range = random.randint(0, 5)
        for spawn in range(0, random_range):  # range should be restrictive
            random_value = random.randint(0, 4)
            car = Turtle()
            car.penup()
            car.shape('shape')
            car.color(COLORS[random_value])
            car.shapesize(stretch_len=2)
            car.setpos(x=320, y=STARTING_POSITIONS[random_value])
        return random_range
    # I need to keep spawning more cars asynchronously to the cars already moving

    def move_cars(self):
        random_car = random.randint(0, 5)
        for car in COLORS:
            # I will probably call "add_car" here.
            if self.cars[COLORS.index(car)].xcor() > - 280:
                random_move = random.randint(2, 15)
                # self.cars[COLORS.index(car)].forward(10 * random_move)
                self.cars[COLORS.index(car)].goto(y=STARTING_POSITIONS[COLORS.index(car)], x=self.cars[COLORS.index(car)].xcor() - random_move)
            else:
                self.cars[COLORS.index(car)].setpos(x=280, y=STARTING_POSITIONS[COLORS.index(car)])
        return

    def add_car(self):
        if car[-1].xcor < 260:
              # I will spawn additional cars in positions excluding the position of the last car or in the position of the last car if the
            # xcor of the last car is beyond a predefined minimum coordinate away from the spawn of the new car.
        return





