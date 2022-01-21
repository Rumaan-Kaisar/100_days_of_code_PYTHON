import datetime as dt
import random

tiMe = dt.datetime.now()

with open("./poem.txt") as qut_file:
    lines = qut_file.readlines()

# weekday() is an object not a variable like hour, year
print(tiMe.weekday())


# -------------  send message  --------------
import smtplib

my_mail = "my_mail@gmail.com"
my_pw = "my_pw"
recipent = "recipent@gmail.com"

if tiMe.weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com") as mail_sender:
        mail_sender.starttls()
        mail_sender.login(user= my_mail, password= my_pw)
        quote_of_the_day = random.choice(lines)
        mail_sender.sendmail(from_addr=my_mail, to_addrs=recipent, msg=f"Subject: Friday Quotes.\n\n{quote_of_the_day}" )


# UnicodeEncodeError: 'ascii' codec can't encode character u'\u2019' in position 3: ordinal not in range(128)

# Fixed with response['source_string'].encode("utf-8")

# python motivation_date_time.py
