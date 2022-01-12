import turtle

tom = turtle.Turtle()
scrn = turtle.Screen()

scrn.colormode(255)

def move_fwrd():
    tom.forward(10)

def move_bkrd():
    tom.back(10)

def move_counter_clockwise():
    tom.right(10)
    #Also:  new_heading = tom.heading() - 10
    #       tom.setheading(new_heading)

def move_clockwise():
    #Also: tom.left(10)
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)


def clear_drawing():
    tom.penup()
    tom.home() # tom.setposition(0.0, 0.0)
    tom.clear()
    tom.pendown()


# turtle.circle(120, 180)  # draw a semicircle

# Listen for an event
scrn.listen()

# Bind an event to the event-listner
scrn.onkey(fun = move_fwrd, key = "w")
scrn.onkey(fun = move_bkrd, key = "s")
scrn.onkey(fun = move_counter_clockwise, key = "a")
scrn.onkey(fun = move_clockwise, key = "d")
scrn.onkey(fun = clear_drawing, key = "c")



scrn.exitonclick()

# python evevnt_lstnr_turtle_scketh_soln.py
