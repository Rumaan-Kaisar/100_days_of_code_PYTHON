import tkinter

wiNdw = tkinter.Tk()

# Title
wiNdw.title("First GUI ????")

# size
wiNdw.minsize(width = 500, height = 300)


my_label_2 = tkinter.Label(text="label", font=("Arial", 24, "italic"))
my_label_2.place(x=300, y=0) 

button_2 = tkinter.Button(text="Click")
button_2.place(x=100, y=200)

input_2 = tkinter.Entry(width=10)
input_2.place(x=200, y=200)



# Grid - layout: It is relative. Relative to first widget

my_label = tkinter.Label(text="label", font=("Arial", 24, "italic"))
my_label.grid(column=0,row=0) 

button = tkinter.Button(text="Click")
button.grid(column=1,row=1)

input = tkinter.Entry(width=10)
input.grid(column=3,row=2)

# challenge
new_button = tkinter.Button(text = "New Button")
new_button.grid(column = 2, row = 0)


# add padding to windows and widgets
wiNdw.config(padx = 20, pady = 20)
new_button.config(padx = 30, pady = 30)


wiNdw.mainloop()

# python tkinter_layout_positioning.py
