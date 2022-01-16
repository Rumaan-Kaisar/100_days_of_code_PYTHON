import tkinter

kms = 0 

winDo = tkinter.Tk()

winDo.minsize(height = 200, width = 300)

inPut = tkinter.Entry(width = 10)
inPut.grid(column = 0, row = 0, padx = 10, pady = 50)

label_1 = tkinter.Label(text = "Miles", font = ("Arial", 24, "normal"))
label_1.grid(column = 1, row = 0)

label_2 = tkinter.Label(text = f"is equal to {kms} km", font = ("Arial", 24, "normal"))
label_2.grid(column = 0, row = 1)

def calc_miles():
    miles = int(inPut.get())
    label_2.config(text = f"is equal to {miles*1.609} km") 

calculate = tkinter.Button(text = "calculate", command = calc_miles)
calculate.grid(column = 0, row = 2)



winDo.mainloop()

# python miles_to_km_GUI.py