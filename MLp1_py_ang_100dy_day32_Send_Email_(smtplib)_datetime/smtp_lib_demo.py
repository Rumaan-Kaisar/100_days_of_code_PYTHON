# ------------- use smtplib to send email straight from python --------------
import smtplib


my_email = "sender@gmail.com"
pasword = "sender_pw"

connection = smtplib.SMTP("smtp.gmail.com")
# TLS makes connection secure
connection.starttls()
connection.login(user = my_email, password = pasword)
connection.sendmail(from_addr = my_email, to_addrs = "reciver@gmail.com", msg = "Subject: Hello Reciver. \n\n Welcome to my Birthday. This is your buddy Sender")
connection.close()

# no "close()" needed if use "with" 

# format for no spam: msg = "Subject: Hello\n\nThis is body".
# Also write normally if you composed in real email.

# Google security Lower
# Photo, 2-step verification turn off
# Turn on - Less secure apps

# Security method could be different in different provider:
# Example :In "yahoo" to allow an app to send email, generates an "app password"



# python smtp_lib_demo.py