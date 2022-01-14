# import turtle

# scrn = turtle.Screen()
# scrn.title("Us State Game")

# image = "./blank_states_img.gif"
# scrn.addshape(image)
# turtle.shape(image)

# scrn.exitonclick()


import turtle
import pandas

scrn = turtle.Screen()
scrn.title("Us State Game")

# setting the map image
scrn.register_shape("./blank_states_img.gif")
tur = turtle.Turtle(shape = "./blank_states_img.gif")

scrn.tracer(0)

# Read CSV data
data = pandas.read_csv("50_states.csv")

game_on =True

while game_on:
    # screen.textinput("NIM", "Name of first player:")
    name = scrn.textinput("Input Name", "Enter the name of a state").capitalize()

    coord = data[data.state == name]
    x = int(coord.x)
    y = int(coord.y)

    tur.speed("fastest")
    tur.color("red")
    tur.penup()

    tur.goto(x, y)
    tur.write(name, align="center", font=('Courier', 10, 'normal'))
    tur.goto(0, 0)
    scrn.update()


# python us_game_main.py
