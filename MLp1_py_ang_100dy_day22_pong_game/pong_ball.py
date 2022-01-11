import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        self.step_x = 10
        self.step_y = 10

        super().__init__() # Always use () 
        # paddle setting
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("#3c412c")

        self.ball_speed = 0.1


    def bounce_y(self):
            self.step_y *= -1
    
    def bounce_x(self):
            self.step_x *= -1
            # increasing speed of the ball by reducing sleep-time : "ball.ball_speed"
            self.ball_speed /= 1.1 

    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.1


# python pong_ball.py.py
