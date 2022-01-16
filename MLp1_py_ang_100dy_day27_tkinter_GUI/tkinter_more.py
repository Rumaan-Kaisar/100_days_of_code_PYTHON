
import tkinter

wiNdw = tkinter.Tk()

# Title
wiNdw.title("First GUI ????")

# size
wiNdw.minsize(width = 500, height = 300)

# Label() and pack()
my_label = tkinter.Label(text= "I am a Label", font=("Courier", 24, "bold"))
# Geometry manager pack() needs to display this label
my_label.pack(side= "bottom")

my_label["text"] = "Hello"

# Setting options in different way
my_label_2 = tkinter.Label(font=("Courier", 24, "bold"))
# Geometry manager pack() needs to display this label
my_label_2.pack(side= "left")

my_label_2.config(text = "Bye !! ")

# --------------- interactivity -----------
# Creating button
# Event-listner funcion for Event-listner
def clicked():
    print("clicked")
    new_label = tkinter.Label()
    new_label.config(text = "Button clicked")
    new_label.pack()

# to make click event use above funtion with command = clicked
button = tkinter.Button(text = "click me", command = clicked)
button.pack()

# Input - field "Entry"
text_input = tkinter.Entry(width = 10)
text_input.pack()

# Grabbing the input
def enter_text():    
    user_input = text_input.get()
    print(user_input)

# to make click event use above funtion with command = clicked
button_2 = tkinter.Button(text = "click me", command = enter_text)
button_2.pack(side = "bottom")


wiNdw.mainloop() #always in end of the program

# python tkinter_more.py







