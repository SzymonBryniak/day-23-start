from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.togo = self.ycor() + MOVE_DISTANCE
        self.setheading(90)

    def go_up(self):
        # self.goto(x=0, y=self.togo)
        self.forward(10)

    def reset_player(self):
        self.setpos(x=0, y=-280)
