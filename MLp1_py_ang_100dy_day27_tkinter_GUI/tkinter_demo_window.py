
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
# fred.pack(side="left")
# fred.pack(expand=1)


wiNdw.mainloop() #always in end of the program

# python tkinter_demo_window.py






# Importing tkinter module
from tkinter import * from tkinter.ttk import *

# creating Tk window
master = Tk()

# creating a Fra, e which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text = "Click me !")
b1.pack(fill = BOTH, expand = True)

# Button 2
b2 = Button(pane, text = "Click me too")
b2.pack(fill = BOTH, expand = True)

# Execute Tkinter
master.mainloop()




# import tkinter module
from tkinter import * from tkinter.ttk import *

# creating main tkinter window/toplevel
master = Tk()

# this wil create a label widget
l1 = Label(master, text = "First:")
l2 = Label(master, text = "Second:")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()





# import tkinter module
from tkinter import * from tkinter.ttk import *

# creating main tkinter window/toplevel
master = Tk()

# this will create a label widget
l1 = Label(master, text = "Height")
l2 = Label(master, text = "Width")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

# checkbutton widget
c1 = Checkbutton(master, text = "Preserve")
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)

# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"C:\Users\Admin\Pictures\capture1.png")
img1 = img.subsample(2, 2)

# setting image with the help of label
Label(master, image = img1).grid(row = 0, column = 2,
	columnspan = 2, rowspan = 2, padx = 5, pady = 5)

# button widget
b1 = Button(master, text = "Zoom in")
b2 = Button(master, text = "Zoom out")

# arranging button widgets
b1.grid(row = 2, column = 2, sticky = E)
b2.grid(row = 2, column = 3, sticky = E)

# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()



# Importing tkinter module
from tkinter import * from tkinter.ttk import *

# creating Tk window
master = Tk()

# setting geometry of tk window
master.geometry("200x200")

# button widget
b1 = Button(master, text = "Click me !")
b1.place(relx = 1, x =-2, y = 2, anchor = NE)

# label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)

# button widget
b2 = Button(master, text = "GFG")
b2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()



# Importing tkinter module
from tkinter import * from tkinter.ttk import *

# creating Tk window
master = Tk()

# setting geometry of tk window
master.geometry("200x200")

# button widget
b2 = Button(master, text = "GFG")
b2.pack(fill = X, expand = True, ipady = 10)

# button widget
b1 = Button(master, text = "Click me !")

# This is where b1 is placed inside b2 with in_ option
b1.place(in_= b2, relx = 0.5, rely = 0.5, anchor = CENTER)

# label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()





