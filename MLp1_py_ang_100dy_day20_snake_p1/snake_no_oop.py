import turtle

# time module for delay the time
import time

scr = turtle.Screen()

# resizing screen
scr.setup(width = 800, height = 700)

# Setting screen color
scr.bgcolor("#a8c64e")

# Showing title of the sreen 
scr.title(" ---- The famous NOKIA 1100 snake game ---- ")

star_positions = [(10, 0), (0, 0), (-10, 0)]


# Turnig off the animation by "tracer" off with "delay" setting
scr.tracer(n = 0)

snake = []

for pos in star_positions:
    sqrs = turtle.Turtle(shape = "square")
    sqrs.shapesize(0.4, 0.4, 0)
    sqrs.color("#3c412c")
    sqrs.penup()
    sqrs._tracer(flag=None)
    sqrs.goto(pos)
        # By default turtle size is 20 X 20. So ours will be 8 X 8. Distance from each other will be 10.
    snake.append(sqrs)

# update the screen after loading the whole snake
scr.update()

game_on = True

while game_on:
    # moving the snake segments. first it will move like a Caterpillar. Need to use "update" and disable "tracer". Update screen here when all snake is moved
    scr.update()
    time.sleep(1)
    
    # Reverse for loop. Move following/backward segments to forward.
    for i in range(len(snake)-1, 0, -1):
        new_x = snake[i-1].xcor()
        new_y = snake[i-1].ycor()
        snake[i].goto(new_x, new_y)
        # Shows one by one move "scr.update()". set higher value with higher "delay" to understand. Shows one by one move slowly: time.sleep(1).
    # moving the first segment
    snake[0].forward(10)

    # snake[0].left(90)

    # Stop the snake at boundary.
    if snake[0].position()[0] >= 380:
        game_on = False

    

# Screen doesn't disappear autometically
scr.exitonclick()

# python snake.py