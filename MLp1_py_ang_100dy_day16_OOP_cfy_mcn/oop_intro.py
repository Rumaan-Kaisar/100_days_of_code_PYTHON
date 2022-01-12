
import prettytable

prettytable.

from turtle import Turtle, Screen

timm = Turtle()
print(timm)
timm.shape("turtle")
timm.color("pink")
for i in range (0, 1000):
    timm.forward(i)
    timm.right(i)

my_scrn = Screen()
print(my_scrn.canvheight)
my_scrn.exitonclick()

# python oop_intro.py