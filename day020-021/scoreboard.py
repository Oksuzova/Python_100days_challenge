from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=('Arial', 36, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal'))
