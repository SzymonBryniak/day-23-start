from turtle import Turtle
FONT = ("Calibri", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = {"loss": 0, "Win": 0}
        self.penup()
        self.hideturtle()

        # self.write(f'Wins: {self.score["Win"]} losses:{self.score["loss"]}', move=True, align="left", font=FONT)

    def update_score(self, val):
        if val < 0:
            self.score["loss"] += 1
        elif val > 0:
            self.score["Win"] += 1
        self.clear()
        self.setpos(-120, 270)
        self.write(f'Wins: {self.score["Win"]} losses:{self.score["loss"]}', move=True, align="left", font=FONT)
        print(self.score)
        return

    def display_score(self):
        self.setpos(-120, 270)
        self.write(f'Wins: {self.score["Win"]} losses:{self.score["loss"]}', move=True, align="left", font=FONT)
        return

