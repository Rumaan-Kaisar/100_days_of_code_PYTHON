import turtle

def mouse_click_coord(x, y):
    print(x, y)


turtle.onscreenclick(mouse_click_coord)

# following runs an infinite loop
turtle.mainloop()

# python mouse_click_stack_overflow.py