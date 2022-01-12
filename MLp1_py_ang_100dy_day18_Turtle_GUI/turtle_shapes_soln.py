import random
from turtle import Screen, Turtle, forward
import turtle

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red", "green")

coLR = ["red", "green", "blue", "black", "violet"]

def shape(sides):
    anGle = 360/sides
    for i in range(0, sides):
        timmy.forward(50)
        timmy.right(anGle)

for shape_side in range(1, 11):
    timmy.pencolor(random.choice(coLR))
    shape(shape_side)

scRen = Screen()
scRen.exitonclick()

# python turtle_shapes_soln.py
