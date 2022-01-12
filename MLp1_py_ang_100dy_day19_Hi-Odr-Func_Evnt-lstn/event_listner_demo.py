import turtle

tom = turtle.Turtle()
scrn = turtle.Screen()

scrn.colormode(255)

def move_fwrd():
    tom.forward(10)

# Listen for an event
scrn.listen()

# Bind an event to the event-listner
scrn.onkey(fun = move_fwrd, key = ".")


scrn.exitonclick()

# python event_listner_demo.py
