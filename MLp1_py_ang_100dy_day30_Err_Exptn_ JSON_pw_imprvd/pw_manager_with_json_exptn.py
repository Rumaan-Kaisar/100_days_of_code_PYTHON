from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Import Json Module
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Create json Data Dictionary format
    new_data = {
        website : {
            "email" : email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:       
        # Now we create a Json file. Change "a" mode to "w" mode. "dump" in "w" mode but "load" in "r" mode
        # "load" in "r" mode
        try:
            with open("data.json", "r") as data_file:
                # Dump "new_data" to json.dump(). Use indent for "readability"
                # json.dump(new_data, data_file, indent=4) # This is SERIALIZE

                # Load old data
                json_data = json.load(data_file) # This is de-SERIALIZE

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving the new data. Notice "json module" is used
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data. Notice the object is used not the "json"
            json_data.update(new_data)

            # "dump" in "w" mode
            with open("data.json", "w") as data_file:
                # Saving the new data. Notice "json module" is used
                json.dump(json_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ----------------- find Password ---------------------

def seArch():
    website = website_entry.get()
    try :
        with open("data.json", "r") as data_file:
                    search_data = json.load(data_file) # This is de-SERIALIZE
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File found .")
    else:
        # We could use "raise" in following for unstored data but if-else doing the job
        if website in search_data:
            email = search_data[website]['email']
            password = search_data[website]['password']
            messagebox.showinfo(title="Found Data", message=f"Email: {email} \n Pasword {password}")
        else:
            messagebox.showinfo(title="Data Notfound", message=f"Sorry There is no data")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_btn = Button(text = "Search", width = 10, command = seArch)
search_btn.grid(row=1, column=2)

window.mainloop()

# python main.py