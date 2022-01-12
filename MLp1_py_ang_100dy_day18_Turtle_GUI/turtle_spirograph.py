import random
from turtle import Screen, Turtle

timmy = Turtle()
scRen = Screen()

scRen.colormode(255)

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)+1):
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.pencolor(rand_color())

draw_spirograph(30)

scRen.exitonclick()

# python turtle_spirograph.py