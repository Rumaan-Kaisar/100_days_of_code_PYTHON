"""
# ----------- Extractiing colors from image -------------
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('Hirst_dots.JPG', 50)


# print(colors[0].Rgb)
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34
"""


# create a list of rgb from extracted color and store the list in a .txt file
"""
cloRs_rgb = []
for i in range(0, len(colors)):
    cloRs_rgb.append(colors[i].rgb)

fiLe = open("extracted_color.txt", "a+")
fiLe.write(str(cloRs_rgb))
"""


# Final list from the extracted_color.txt file

def Rgb(r, g, b):
    tuP = (r, g, b)
    return tuP

extracted_color = [Rgb(r=239, g=236, b=238), Rgb(r=239, g=237, b=235), Rgb(r=235, g=237, b=242), Rgb(r=229, g=238, b=232), Rgb(r=26, g=109, b=164), Rgb(r=191, g=39, b=81), Rgb(r=234, g=160, b=54), Rgb(r=233, g=214, b=88), Rgb(r=220, g=137, b=175), Rgb(r=142, g=108, b=57), Rgb(r=105, g=195, b=217), Rgb(r=204, g=165, b=30), Rgb(r=20, g=57, b=131), Rgb(r=212, g=75, b=92), Rgb(r=235, g=89, b=51), Rgb(r=119, g=190, b=141), Rgb(r=140, g=28, b=72), Rgb(r=141, g=207, b=225), Rgb(r=105, g=107, b=195), Rgb(r=7, g=157, b=87), Rgb(r=7, g=184, b=175), Rgb(r=97, g=50, b=36), Rgb(r=21, g=162, b=203), Rgb(r=228, g=169, b=188), Rgb(r=30, g=91, b=94), Rgb(r=85, g=46, b=34), Rgb(r=31, g=44, b=85), Rgb(r=174, g=185, b=224), Rgb(r=150, g=214, b=193), Rgb(r=234, g=173, b=162), Rgb(r=29, g=94, b=93), Rgb(r=241, g=200, b=5), Rgb(r=97, g=22, b=52)]

print(f"extracted_color : {extracted_color}, and length : {len(extracted_color)}")

from turtle import Screen, Turtle
import random

tim = Turtle()
scr = Screen()

scr.colormode(255)
dot_size = 20
step_size = 40

tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.left(225)
tim.forward(198)
tim.right(225)

for i in range(1, 50):
    # tim.pencolor((23, 45, 67))
    tim.dot(dot_size, random.choice(extracted_color))
    tim.forward(step_size)
    if i%7 == 0:
        tim.left(90)
        tim.forward(step_size)
        tim.left(90)
        tim.forward(7*step_size)
        tim.left(180)


scr.exitonclick()

# python hirsts_colordots.py