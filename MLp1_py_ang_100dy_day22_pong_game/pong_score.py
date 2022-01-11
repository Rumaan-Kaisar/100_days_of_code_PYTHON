import turtle
# from turtle import Screen 

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color("#3c412c")
        self.show_score()

    def show_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, move= False, align= "center", font= ("Courier", 80, "normal"))
        
        self.goto(100, 200)
        self.write(self.r_score, move= False, align= "center", font= ("Courier", 80, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.show_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.show_score()

# python pong_score.py
