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
    
    # create_sanke(self), add_segments(self, position) creates the snake body first

    def create_sanke(self):
        for pos in STARTING_POSITION:
            self.add_segments(pos)

    def add_segments(self, position):
            sqrs = turtle.Turtle(shape = "square")
            sqrs.shapesize(0.4, 0.4, 0)
            sqrs.color("#3c412c")
            sqrs.penup()
            sqrs.goto(position)
                # By default turtle size is 20 X 20. So ours will be 8 X 8. Distance from each other will be 10.
            self.snake.append(sqrs)

    # Extend the body when collide with food
    def extend_body(self):
        # "-1" is used to indicate the "last" element of the list
        self.add_segments(self.snake[-1].position())

    def move(self):    
        # Reverse for loop. Move following/backward segments to forward.
        for i in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].goto(new_x, new_y)
            # Shows one by one move "scr.update()". set higher value with higher "delay" to understand. Shows one by one move slowly: time.sleep(1).
        # moving the first segment
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):

        for seg in self.snake:
            seg.goto(1000, 1000)

        # Clearing the array
        self.snake.clear()
        self.create_sanke()
        self.head = self.snake[0]
        # self.move() not needed while-loop in main will do the job

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