import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.turtlesize(0.4, 0.4)
        self.penup()
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-300, 300)
        self.goto(random_x, random_y)

# python food.py