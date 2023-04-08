from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Cooper Black", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setposition(0, 270)
        self.write(f"Scoreboard {self.score}", align=ALIGNMENT,
                   font=("Cooper Black", 20, "normal"))
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Scoreboard {self.score}", align="center",
                   font=FONT)
    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
