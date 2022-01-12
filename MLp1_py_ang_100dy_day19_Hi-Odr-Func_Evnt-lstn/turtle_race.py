import turtle
import random

scrn = turtle.Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
# use setup() instead of screensize()
scrn.setup(1200, 650)

user_guess = scrn.textinput("Guess the Turtle", "Guess which Turtle gonna win: ").lower()


y_pos = [-225, -150, -75, 0, 75, 150, 225]

all_turtle = []

for turtle_index in range (0, 7):
    # Notice we are actually declaring "Turrle" object with "shape"
    new_turtle = turtle.Turtle(shape= "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -575, y = y_pos[turtle_index])
    all_turtle.append(new_turtle)

print(f"You choose : {user_guess}")


if user_guess:
    game_on = True

# match fixing
all_turtle[3].forward(100)

while game_on:
    for trtl in all_turtle:
        random_number = random.randint(0, 10)
        trtl.forward(random_number)
        if trtl.position()[0] >= 590:
            game_on = False
            winner_color = trtl.pencolor()
            print(f"The \' {trtl.pencolor()} \'Turtle wins")
            if winner_color == user_guess:
                print("you win the bet")
            else:
                print("You lost the bet :( ")

# notice how y-position is retrived from the returned "tuple" from "fromposition()"
# print(all_turtle[6].position()[1])

scrn.exitonclick()

# python turtle_race.py
