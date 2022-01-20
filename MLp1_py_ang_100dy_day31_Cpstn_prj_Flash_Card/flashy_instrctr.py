import tkinter
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict_list = []

# Open CSV file and store it to a dictionary
import pandas

try:
    data = pandas.read_csv("./data/learned.csv")
    data_dict_list = data.to_dict(orient = "records")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    # create dictionary-list and ORIENT-Data-dictionary
    data_dict_list = original_data.to_dict(orient = "records")


# ------------------------ window and Canvas ----------------------
winDoW = tkinter.Tk()
winDoW.title("Flashy")
winDoW.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)

# Must use required keyword
iMaGe_back = tkinter.PhotoImage(file = "./images/card_back.png")
iMaGe_front = tkinter.PhotoImage(file = "./images/card_front.png")


cAnVas = tkinter.Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
back_ground= cAnVas.create_image(400, 263, image = iMaGe_front)
cAnVas.grid(row = 0, column = 0, columnspan = 2)


def flip_card():
    cAnVas.itemconfig(lang, text = "English", fill = "white")
    cAnVas.itemconfig(word, text = current_card["English"], fill = "white")
    cAnVas.itemconfig(back_ground, image = iMaGe_back)

flip_timer = winDoW.after(3000, flip_card)

def next_card():
    global current_card, flip_timer
    winDoW.after_cancel(flip_timer)
    current_card = random.choice(data_dict_list)
    
    cAnVas.itemconfig(lang, text = "French", fill = "black", font = ("Arial", 18, "italic"))
    cAnVas.itemconfig(word, text = current_card["French"], fill = "black", font = ("Arial", 28, "bold"))
    cAnVas.itemconfig(back_ground, image = iMaGe_front)
    flip_timer = winDoW.after(3000, flip_card)

def is_known():
    data_dict_list.remove(current_card)
    data_frm = pandas.DataFrame(data_dict_list)
    # To get rid of indexing each time during save use "index=False"
    data_frm.to_csv("./data/learned.csv", index=False)
    next_card()


# ------------------- Buttons -------------------
known_btn_img = tkinter.PhotoImage(file = "./images/right.png")
known_btn = tkinter.Button(image = known_btn_img, bd = 0, highlightthickness=0)
known_btn.config(command = is_known)
known_btn.grid(row = 1, column = 1, padx = 100, pady = 20)

unknown_btn_img = tkinter.PhotoImage(file = "./images/wrong.png")
unknown_btn = tkinter.Button(image = unknown_btn_img, bd = 0, highlightthickness=0)
unknown_btn.config(command = next_card)
unknown_btn.grid(row = 1, column = 0, padx = 100, pady = 20)


# -------------- Labels: Show the words ----------
lang = cAnVas.create_text(400, 150, font = ("Arial", 40, "italic"))
word = cAnVas.create_text(400, 263, font = ("Arial", 60, "bold"))

next_card()

winDoW.mainloop()

# python flashy_instrctr.py

