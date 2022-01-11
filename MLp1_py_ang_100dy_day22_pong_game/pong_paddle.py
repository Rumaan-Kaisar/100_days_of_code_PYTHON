import turtle
STEP = 20

class Paddle(turtle.Turtle):
    def __init__(self, posITon):
        super().__init__() # Always use () 
        # paddle setting
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5) 
        self.speed("fastest")
        self.penup()
        self.color("#3c412c")
        self.goto(posITon)



    def change_pos(self, step):
        x_crd = self.xcor()
        y_crd = self.ycor()
        self.goto(x_crd, y_crd + step)

    def up(self):
        self.change_pos(STEP)

    def down(self):
        self.change_pos(-STEP)

# python pong_paddle.py
