import turtle

STARTING_POSITION = (0, -330)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 330


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.go_to_start_position()
        self.setheading(90)

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)

    def move_forwrd(self):
        self.forward(MOVE_DISTANCE)
    
    def move_back(self):
        self.backward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
