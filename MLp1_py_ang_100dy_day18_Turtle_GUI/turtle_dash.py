from turtle import Screen, Turtle, forward

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red", "green")

for i in range(0, 50):
    if i%2 == 0:
        timmy.pendown()
        timmy.forward(10)
    else:
        timmy.penup()
        timmy.forward(10)


scRen = Screen()
scRen.exitonclick()

# python turtle_square.py
