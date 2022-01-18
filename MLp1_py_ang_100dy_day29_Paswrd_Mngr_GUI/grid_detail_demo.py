import tkinter

winDow = tkinter.Tk()

labl_1 = tkinter.Label(width = 20, height= 5, bg = "red")
labl_1.grid(column = 0, row = 0)

labl_2 = tkinter.Label(width = 20, height= 5, bg = "green")
labl_2.grid(column = 1, row = 1)

# simply increasing the width of an elment not gonna work.
# It just make the column wider
# We need to use "columnspan" attribute along with increased width
labl_3 = tkinter.Label(width = 40, height= 5, bg = "blue")
labl_3.grid(column = 0, row = 2, columnspan = 2)


winDow.mainloop()
# python grid_detail_demo.py