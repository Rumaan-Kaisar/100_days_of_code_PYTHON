import turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#3c412c")
        self.penup()
        self.speed("fastest")
        self.goto(0, 310)
        self.score = 0
        self.update_scoreboard()

    def gameover(self):
        self.goto(0 , 0)
        self.write(f"GAME OVER", move= False, align= ALIGNMENT, font= FONT)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", move= False, align= ALIGNMENT, font= FONT)

    def icrease_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
# python scoreboard.py