from tkinter import *
import requests


def get_quote():
    
    #Write your code here.
    reQest = requests.get(url = "https://api.kanye.rest")
    reQest.raise_for_status()
    data = reQest.json()
    print(data["quote"])
    canvas.itemconfig(quote_text, text = data["quote"])




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background_2.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="#be2edd")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye_2.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bd = 0)
kanye_button.grid(row=1, column=0)



window.mainloop()


# python kanye_main.py