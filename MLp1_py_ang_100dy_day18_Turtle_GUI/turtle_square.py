from turtle import Screen, Turtle

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red", "green")

for i in range(0, 4):
    timmy.forward(100)
    timmy.right(90)


scRen = Screen()
scRen.exitonclick()

# python turtle_square.py
