"""
# ----------- Extractiing colors from image -------------
import colorgram

rgb_colosr = []
colors = colorgram.extract('Hirst_dots.JPG', 50)

for clrs in colors:
    r = clrs.rgb.r
    g = clrs.rgb.g
    b = clrs.rgb.b

    new_colour = (r, g, b)
    rgb_colosr.append(new_colour)

print(rgb_colosr)

"""


rgb_colors = [(239, 236, 238), (239, 237, 235), (235, 237, 242), (229, 238, 232), (26, 109, 164), (191, 39, 81), (234, 160, 54), (233, 214, 88), (220, 137, 175), (142, 108, 57), (105, 195, 217), (204, 165, 30), (20, 57, 131), (212, 75, 92), (235, 89, 51), (119, 190, 141), (140, 28, 72), (141, 207, 225), (105, 107, 195), (7, 157, 87), (7, 184, 175), (97, 50, 36), (21, 162, 203), (228, 169, 188), (30, 91, 94), (85, 46, 34), (31, 44, 85), (174, 185, 224), (150, 214, 193), (234, 173, 162), (29, 94, 93), (241, 200, 5), (97, 22, 52)]


import turtle
import random

tim = turtle.Turtle()
scr = turtle.Screen()
scr.colormode(255)

tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


scr.exitonclick()

# python hirsts_colordots_ins_soln.py