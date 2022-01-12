import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Reduce the car number by random choice.
        if random.randint(1, 6) == 3:
            self.car = turtle.Turtle(shape= "square")
            self.car.penup()
            self.car.color(random.choice(COLORS))
            self.car.shapesize(stretch_len= 2, stretch_wid= 1)
            rand_y = random.randint(-300, 300)
            self.car.goto(350, rand_y)
            self.all_cars.append(self.car)
        

    def move_cars(self):
        for cAr in self.all_cars:
            cAr.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


# (0.1 + random.random())
# self.shapesize(stretch_len= 2 + 3*(0.1 + random.random()) , stretch_wid= 2*(0.1 + random.random()))