import turtle
import snake
# time module for delay the time
import time

scr = turtle.Screen()

# resizing screen. Setting screen color. Showing title of the sreen 
scr.setup(width = 800, height = 700)
scr.bgcolor("#a8c64e")
scr.title(" ---- The famous NOKIA 1100 snake game ---- ")

# Turnig off the animation by "tracer" off with "delay" setting
scr.tracer(n = 0)

# create a snake object
snAKe = snake.Snake()

# update the screen after loading the whole snake
scr.update()


scr.listen()
scr.onkey(snAKe.up, "Up")
scr.onkey(snAKe.down, "Down")
scr.onkey(snAKe.left, "Left")
scr.onkey(snAKe.right, "Right")


game_on = True

while game_on:
    # moving the snake segments. first it will move like a Caterpillar. Need to use "update" and disable "tracer". Update screen here when all snake is moved
    scr.update()
    time.sleep(0.2)
    
    snAKe.move()

    # snake[0].left(90)

    # Stop the snake at boundary.
    if snAKe.snake[0].position()[0] >= 380:
        game_on = False

    

# Screen doesn't disappear autometically
scr.exitonclick()

# python snake_main.py