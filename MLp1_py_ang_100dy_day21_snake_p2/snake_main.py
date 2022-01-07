import turtle
import snake
import food
import scoreboard
import border
# time module for delay the time
import time

scr = turtle.Screen()

# resizing screen. Setting screen color. Showing title of the sreen 
scr.setup(width = 830, height = 700)
scr.bgcolor("#a8c64e")
scr.title(" ---- The famous NOKIA 1100 snake game ---- ")

# Turnig off the animation by "tracer" off with "delay" setting
scr.tracer(n = 0)

# create a snake object
snAKe = snake.Snake()
foOd = food.Food()
brDr = border.Border()
scrBrd = scoreboard.Scoreboard()

# update the screen after loading the whole snake
scr.update()


scr.listen()
scr.onkey(snAKe.up, "Up")
scr.onkey(snAKe.down, "Down")
scr.onkey(snAKe.left, "Left")
scr.onkey(snAKe.right, "Right")


game_on = True

score = 0

while game_on:
    # moving the snake segments. first it will move like a Caterpillar. Need to use "update" and disable "tracer". Update screen here when all snake is moved
    scr.update()
    time.sleep(0.1)
    
    snAKe.move()

    # Collition with food
    if (snAKe.head.distance(foOd)) <= 10:
        score += 1
        print("noom noom !!!")
        foOd.refresh()
        snAKe.extend_body()
        scrBrd.icrease_score()

    # snake[0].left(90)

    # Wall Collision: Stop the snake at boundary.
    if (snAKe.head.xcor() >= 360) or (snAKe.head.xcor() <= -360) or (snAKe.head.ycor() >= 310) or (snAKe.head.ycor() <= -310):
        scrBrd.gameover()
        game_on = False

    # Detect collision with tail.
    # if head collides with any segment in the tail 
    # # trigger game.over
    # ------ can be done with "slicing the list"
    for sQr_segmnt in snAKe.snake[1 : ]:
        if snAKe.head.distance(sQr_segmnt) < 10 :
            scrBrd.gameover()
            game_on = False

    

# Screen doesn't disappear autometically
scr.exitonclick()

# python snake_main.py
