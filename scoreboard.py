from turtle import Turtle
FONT = ("Calibri", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = {"loss": 0, "Win": 0, "Level": 1}
        self.penup()
        self.hideturtle()

    def update_score(self, val):
        if val < 0:
            self.score["loss"] += 1
        elif val > 0:
            self.score["Win"] += 1
        self.clear()
        self.setpos(-120, 265)
        self.display_score()
        self.display_level()
        print(self.score)

    def update_level(self):
        self.score["Level"] += 1
        self.clear()
        self.display_level()
        self.display_score()

    def display_score(self):
        self.setpos(-120, 265)
        self.write(f'Wins: {self.score["Win"]} losses:{self.score["loss"]}', move=True, align="left", font=FONT)

    def display_level(self):
        self.setpos(-250, 265)
        self.write(f'Level: {self.score["Level"]}', move=True, align="left", font=FONT)
