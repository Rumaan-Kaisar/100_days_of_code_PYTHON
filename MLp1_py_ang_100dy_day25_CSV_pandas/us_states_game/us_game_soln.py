import turtle
import pandas

scrn = turtle.Screen()
scrn.title("Us State Game")

image = "./blank_states_img.gif"
scrn.addshape(image)
turtle.shape(image)


scrn.tracer(0)

# Read CSV data
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50 :
    # screen.textinput("NIM", "Name of first player:")
    name = (scrn.textinput(title= f"{len(guessed_state)}/50 States Correct",prompt= "Enter the name of a state")).title()
        # "list" is needed to check "name" inside the "data" so we converted "data.state" to "list"
    if name == "Exit":
        missed_states = []
        # Create a missed states CSV
        for staTe in all_states:
            if staTe not in guessed_state:
                missed_states.append(staTe)
        print(missed_states)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    elif name in all_states:
        guessed_state.append(name)
        tur = turtle.Turtle()
        tur.speed("fastest")
        tur.color("red")
        tur.penup()
        tur.hideturtle()

        found_state = data[data.state == name]
        tur.goto(int(found_state.x), int(found_state.y))
        tur.write(found_state.state.item(), align="center", font=('Courier', 10, 'normal'))
        
        scrn.update()


# python us_game_soln.py
