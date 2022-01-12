import turtle

STARTING_POSITION = [(10, 0), (0, 0), (-10, 0)]
MOVE_DISTANCE = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_sanke()
        self.head = self.snake[0] # This line is called after create_sanke(), unless error occurs
    
    def create_sanke(self):
        for pos in STARTING_POSITION:
            sqrs = turtle.Turtle(shape = "square")
            sqrs.shapesize(0.4, 0.4, 0)
            sqrs.color("#3c412c")
            sqrs.penup()
            sqrs.goto(pos)
                # By default turtle size is 20 X 20. So ours will be 8 X 8. Distance from each other will be 10.
            self.snake.append(sqrs)


    def move(self):    
        # Reverse for loop. Move following/backward segments to forward.
        for i in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].goto(new_x, new_y)
            # Shows one by one move "scr.update()". set higher value with higher "delay" to understand. Shows one by one move slowly: time.sleep(1).
        # moving the first segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# python snake.py