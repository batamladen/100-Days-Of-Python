from turtle import Turtle

ALINGMENT = 'center'
FONT = ('Times New Roman', 24, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0,260)

    def start_scorebord(self):
        self.write(arg=f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def increase_scoreboard(self):
        self.clear()
        self.score +=1
        self.start_scorebord()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALINGMENT, font=FONT)
