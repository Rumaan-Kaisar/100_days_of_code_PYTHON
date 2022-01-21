import random
import pandas
import datetime as DaTe
import smtplib

PLACEHOLDER = "[NAME]"


letter_no = random.randint(1, 3)

letter_file = f"./letter_templates/letter_{letter_no}.txt"

with open(letter_file) as to_send:
    leTTer = to_send.read()



data = pandas.read_csv("birthdays_2.csv")

today = DaTe.datetime.now()

moNth = today.month
dAy = today.day



# print(type(moNth))
# print(moNth)
# print(type(dAy))
# print(dAy)

my_mAI = "my_mAI"
my_pw = "my_pw"

# Check if the row is empty
rOw = data[(data.day == dAy) & (data.month == moNth)]
if rOw.empty:
    print("Empty")
else:
    name = rOw.name.item()
    EmIl = rOw.email.item()
    newL = leTTer.replace(PLACEHOLDER, name)
    print(newL)
    print(name)
    print(EmIl)
    with smtplib.SMTP("smtp.gmail.com") as sender:
        sender.starttls()
        sender.login(user= my_mAI, password=  my_pw)
        sender.sendmail(from_addr= my_mAI, to_addrs= EmIl, msg = f"Subject: Birthday Wish\n\n {newL} At the END")




# python bdy_wisher.py