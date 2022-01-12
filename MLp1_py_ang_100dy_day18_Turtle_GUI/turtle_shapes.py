from turtle import Screen, Turtle, forward

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red", "green")

for i in range(1, 11):
    if i%2 == 0:
        timmy.pencolor("red")
    elif i%3 == 0:
        timmy.pencolor("green")

    for j in range(0,i):
        timmy.forward(50)
        timmy.right(360/i)



scRen = Screen()
scRen.exitonclick()

# python turtle_shapes.py
