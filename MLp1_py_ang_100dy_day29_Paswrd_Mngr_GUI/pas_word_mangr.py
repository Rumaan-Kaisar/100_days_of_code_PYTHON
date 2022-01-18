import tkinter
from tkinter import messagebox
from tkinter import END
import random
import pyperclip
# END index: END only works if you did "from Tkinter import *". If you haven't imported everything from Tkinter, then you need to do "tk.END" instead.


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    rand_letter = [random.choice(letters) for n in range(nr_letters)]
    rand_symbols = [random.choice(symbols) for n in range(nr_symbols)]
    rand_numbers = [random.choice(numbers) for n in range(nr_numbers)]


    password_list = rand_letter + rand_symbols + rand_numbers
    random.shuffle(password_list)

    # Python String join() Method
    password = ''.join(password_list)

    # Fill the password in the password field
    if len(pas_wrd_entry.get()) == 0:
        pas_wrd_entry.insert(0, password)
        pyperclip.copy(password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #

# END index: END only works if you did "from Tkinter import *". If you haven't imported everything from Tkinter, then you need to do "tk.END" instead.

# ====== Creates Line entry ======
def save_data():
    web_data = web_site_entry.get()
    eml_usr_data = emai_unam_entry.get()
    pw_data = pas_wrd_entry.get()

    if len(web_data) < 1:
        messagebox.showinfo(title= "Unacceptable", message="Plesase Enter a Website")
    elif len(eml_usr_data) < 1:
        messagebox.showinfo(title= "Unacceptable", message="Plesase Enter your email address")
    elif len(pw_data) < 1: 
        messagebox.showinfo(title= "Unacceptable", message="Plesase Enter password")
    else:
        is_ok = messagebox.askokcancel(title= "Upload Info", message="Uplod the data ?")
    
        if is_ok:
            print(f"web: {web_data},\n usr :{eml_usr_data},\n pw: {pw_data}")
            with open(file= "data.txt", mode= "a+") as data_file:
                data_file.write(f"{web_data} | {eml_usr_data} | {pw_data}\n")
            
            web_site_entry.delete(0, END)
            pas_wrd_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
wiNdow = tkinter.Tk()
wiNdow.config(padx = 50, pady = 50)
wiNdow.title("Password Manager")


# "PhotoImage" is a tkinter class like "Tk". Corruptet image gives error.
lo_go = tkinter.PhotoImage(file="./logo_3.png")

# Image input
canVas = tkinter.Canvas(width = 200, height = 200)
canVas.create_image(100, 100, image= lo_go)
canVas.grid(column = 1, row = 0)

# UI Layout
# width of the row widest column is 32unit. 200px will be considered 32
# labels and Inputs
web_site = tkinter.Label(text = "Website : ")
web_site.grid(column= 0, row= 1, sticky = 'w') 
web_site_entry = tkinter.Entry(width = 52)
# draw focus/cursor
web_site_entry.focus()
web_site_entry.grid(column= 1, row= 1, columnspan = 2, sticky = 'w')

emai_unam = tkinter.Label(text = "Email/Username : ")
emai_unam.grid(column= 0, row= 2, sticky = 'w')
emai_unam_entry = tkinter.Entry(width = 52)
# make default fillup insert(): 0 or END as index and a fillfup string 
emai_unam_entry.insert(0, "example@site.com")
emai_unam_entry.grid(column= 1, row= 2, columnspan = 2, sticky = 'w')

pas_wrd = tkinter.Label(text = "Password : ")
pas_wrd.grid(column= 0, row= 3, sticky = 'w')
pas_wrd_entry = tkinter.Entry(width = 32)
pas_wrd_entry.grid(column= 1, row= 3, sticky = 'w')

# Buttons
gen_pw_btn = tkinter.Button(text = "Generate Pasword", command = password_generator)
gen_pw_btn.grid(column= 2, row= 3, sticky = 'w')
add_btn = tkinter.Button(text = "add", width = 44)
# Genetate event
add_btn.config(command = save_data)
add_btn.grid(column= 1, row= 4, columnspan = 2, sticky = 'w')

# sticky = 'w' and sticky = 'e' are used with grid to left/right align



wiNdow.mainloop()

#  python pas_word_mangr.py

