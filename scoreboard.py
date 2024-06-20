from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", align="left", font=FONT)


    def update_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="Center", font=FONT)
    
