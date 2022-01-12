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

directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    timmy.width(15)
    timmy.speed("fastest")
    timmy.pencolor(rand_color())

scRen.exitonclick()

# python turtle_ran_wlk.py
