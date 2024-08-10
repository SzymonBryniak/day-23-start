from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITIONS = [-240, -125, -140, -40, 60, 160, 260]
RANDOM_VALUE = random.randint(0, 5)


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
        random_value = random.randint(0, 5)
        car = Turtle()
        car.penup()
        car.shape('square')
        car.color(COLORS[random_value])
        car.shapesize(stretch_len=2)
        car.setpos(x=320, y=STARTING_POSITIONS[random_value])
        self.cars.append(car)

    def move_cars(self):
        random_position = random.randint(0, 5)
        self.create_car()
        for car in range(0, len(self.cars)):
            # I will probably call "add_car" here.
            if self.cars[car].xcor() > -280:
                random_move = random.randint(2, 15)
                # self.cars[COLORS.index(car)].forward(10 * random_move)
                self.cars[car].goto(y=self.cars[car].ycor(), x=self.cars[car].xcor() - random_move)
            else:
                self.cars[car].setpos(x=280, y=self.cars[car].ycor())

        return

    # def add_car(self, number_of_cars):
    #     self.create_car()
    #     random_value = random.randint(0, 5)
    #     random_postion = STARTING_POSITIONS[random_value]
    #     starting_position = 0
    #     cars = len(self.cars)
    #     for car in range(0 , cars):
    #         if player.distance(cars.cars[i]) < 25 and player.xcor():
    #             continue
    #     if self.cars[
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





