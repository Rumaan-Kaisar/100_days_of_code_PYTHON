import turtle

scrn = turtle.Screen()
scrn.title("Us State Game")

image = "./blank_states_img.gif"
scrn.addshape(image)
turtle.shape(image)

tur = turtle.Turtle()

# turtle.onscreenclick(fun, btn=1, add=None)
    # Parameters
        # fun = a function with two arguments which will be called with the coordinates of the clicked point on the canvas

        # btn = number of the mouse-button, defaults to 1 (left mouse button)

        # add = True or False . if True, a new binding will be added, otherwise it will replace a former binding

# Eg: screen.onclick(turtle.goto)



def mouse_click_coord(x, y):
    print(x, y)

for i in range(0, 10):
    scrn.onscreenclick(mouse_click_coord)

# follown runs an infinite loop
turtle.mainloop()

# python mouse_click.py