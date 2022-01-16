import tkinter

def calc_miles():
    miles = float(miles_inPut.get())
    print(miles*1.609)
    km_result_label.config(text = f"{str(miles*1.609)}") 

winDo = tkinter.Tk()
winDo.title("Miles to Kilometer converter")

winDo.minsize(height = 200, width = 300)
winDo.config(padx = 20, pady =20)

miles_inPut = tkinter.Entry(width = 7)
miles_inPut.grid(column = 1, row = 0, padx = 10, pady = 50)

miles_label = tkinter.Label(text = "Miles", font = ("Arial", 24, "normal"))
miles_label.grid(column = 2, row = 0)


isequal_label = tkinter.Label(text = f"is equal to", font = ("Arial", 24, "normal"))
isequal_label.grid(column = 0, row = 1)



km_label = tkinter.Label(text = "km", font = ("Arial", 24, "normal"))
km_label.grid(column = 2, row = 1)




calculate = tkinter.Button(text = "calculate", command = calc_miles)
calculate.grid(column = 1, row = 2)

km_result_label = tkinter.Label(text = "0", font = ("Arial", 24, "normal"))
km_result_label.grid(column = 1, row = 1)


winDo.mainloop()

# python miles_to_km_GUI_soln.py