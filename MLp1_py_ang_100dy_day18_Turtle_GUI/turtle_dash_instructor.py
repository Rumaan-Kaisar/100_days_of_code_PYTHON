from turtle import Screen, Turtle, forward

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red", "green")

for i in range(0, 50):
        timmy.pendown()
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)


scRen = Screen()
scRen.exitonclick()

# python turtle_dash_instructor.py
