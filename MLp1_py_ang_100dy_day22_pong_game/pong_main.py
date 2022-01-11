import turtle
import pong_paddle
import pong_ball
import pong_score
import time

scr_een = turtle.Screen()


# Backgrund color : "#a8c64e" and Turtle color: "#3c412c"
scr_een.title("PONG")
scr_een.bgcolor("#a8c64e")
scr_een.setup(width= 800, height= 600)

# animation modification
scr_een.tracer(0)

# Paddle setup
# Notice Tuple is used
r_paddle = pong_paddle.Paddle((350, 0))
l_paddle = pong_paddle.Paddle((-350, 0))


# Ball setup. Use tuple for position
ball = pong_ball.Ball()

# Score
score = pong_score.Score()

scr_een.listen()

scr_een.onkeypress(r_paddle.up, "Up")
scr_een.onkeypress(r_paddle.down, "Down")

scr_een.onkeypress(l_paddle.up, "Left")
scr_een.onkeypress(l_paddle.down, "Right")

gam_is_on = True
while gam_is_on:
    scr_een.update()
    time.sleep(ball.ball_speed)

    # collision with wall
    if (ball.ycor() >= 280) or (ball.ycor() <= -280):
        ball.bounce_y()

    # collision with Paddle and out of bound
    if (ball.distance(r_paddle) < 42) and (ball.xcor() >= 330):
        ball.bounce_x()
    elif (ball.distance(l_paddle) < 42) and (ball.xcor() <= -330):
        ball.bounce_x()




    # Benefit of doing seperately: For updating the score
    # Detect R paddle misses
    if ball.xcor() >= 360:
        ball.reset_position()
        score.l_point()

    # Detect R paddle misses
    if ball.xcor() <= -360:
        ball.reset_position()
        score.r_point()

    ball.move()

scr_een.exitonclick()

# python pong_main.py
