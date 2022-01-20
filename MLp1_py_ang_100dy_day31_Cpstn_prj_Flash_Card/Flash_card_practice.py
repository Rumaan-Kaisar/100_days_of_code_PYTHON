import tkinter
import random

BACKGROUND_COLOR = "#B1DDC6"
RED = "#e7305b"
ini_word = ()

# Open CSV file and store it to a dictionary
import pandas

data = pandas.read_csv("./data/french_words.csv")
print(data)

        # create dictionary
data_dict = data.to_dict()
print(data_dict)

# ----------------  Random-Choice of French word ---------------------
def random_word():
    ran_num = random.randint(0, 100)
    print(ran_num)
    french = data_dict["French"][ran_num]
    english = data_dict["English"][ran_num]
    return (french, english)
#     ask = input(f"Know the Feench word '{french}' ? y/n :").lower()
#     if ask == "n":
#         print(f"The english word is : '{english}'")
#         random_word()
#     elif ask == "y":
#         random_word()
#     else:
#         print("wrong key")

# random_word()


# ------------------- button clicks : Card flip ----------------------

def flip():
    global ini_word
    cAnVas.itemconfig(back_ground, image = small_front)
    # create new text
    cAnVas.itemconfig(lang, text = "English", fill = "black", font = ("Arial", 18, "italic"))
    cAnVas.itemconfig(word, text = f"\n {ini_word[1]}", fill = "black", font = ("Arial", 28, "bold"))

def genrt_word():
    global ini_word
    ini_word = random_word()
    cAnVas.itemconfig(back_ground, image = small_back)
    cAnVas.itemconfig(lang, text = "French", fill = "white", font = ("Arial", 18, "italic"))
    cAnVas.itemconfig(word, text = f"\n {ini_word[0]}", fill = "white", font = ("Arial", 28, "bold"))




# ------------------------ window and Canvas ----------------------
winDoW = tkinter.Tk()
winDoW.title("Flash Card : Learn French")
winDoW.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)

# Must use required keyword
iMaGe_back = tkinter.PhotoImage(file = "./images/card_back.png")
iMaGe_front = tkinter.PhotoImage(file = "./images/card_front.png")

# Image resize with subsample(): +ve higher value smaller
small_back = iMaGe_back.subsample(2, 2) # Image resize
small_front = iMaGe_front.subsample(2, 2) # Image resize

cAnVas = tkinter.Canvas(width = 400, height = 263, bg = BACKGROUND_COLOR, highlightthickness=0)
back_ground= cAnVas.create_image(200, 132, image = small_back)
cAnVas.grid(row = 0, column = 1)



# ------------------- Buttons -------------------
right_btn_img = tkinter.PhotoImage(file = "./images/right.png")
rightButtonResizedImage = right_btn_img.subsample(2, 2)
right_btn = tkinter.Button(image = rightButtonResizedImage, bd = 0, highlightthickness=0)
right_btn.config(command = genrt_word)
right_btn.grid(row = 2, column = 1, sticky = 'w', padx = 100, pady = 20)

wrong_btn_img = tkinter.PhotoImage(file = "./images/wrong.png")
wrongButtonResizedImage = wrong_btn_img.subsample(2, 2)
wrong_btn = tkinter.Button(image = wrongButtonResizedImage, bd = 0, highlightthickness=0)
wrong_btn.config(command = flip)
wrong_btn.grid(row = 2, column = 1, sticky = 'e', padx = 100, pady = 20)


# -------------- Labels: Show the words ----------
ini_word = random_word()
lang = cAnVas.create_text(200, 100, text = "French", fill = "white", font = ("Arial", 18, "italic"))
word = cAnVas.create_text(200, 132, text = f"\n {ini_word[0]}", fill = "white", font = ("Arial", 28, "bold"))

# auto genetate a word after 3secs or 3000 mili-secs
def auto_generate(coUnt):
    if coUnt > 0:
        genrt_word()
        winDoW.after(3000, auto_generate, coUnt-1)

auto_generate(100)

# meaning_label = tkinter.Label(text = , font = ("Arial", 30, "bold"), fg = RED )
# meaning_label.grid(row = 1, column = 1)


winDoW.mainloop()



# python Flash_card_practice.py


# Image resize
# scale_w = new_width/old_width
# scale_h = new_height/old_height
# photoImg.zoom(scale_w, scale_h)
# or use 
# iMaGe.subsample()