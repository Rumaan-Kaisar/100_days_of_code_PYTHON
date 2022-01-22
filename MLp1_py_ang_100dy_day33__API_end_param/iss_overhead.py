import requests
from datetime import datetime
import smtplib
import time

My_email = ""
My_pw = ""


MY_LAT = 23.835852 # Your latitude
MY_LONG = 90.252404 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


#If the ISS is close to my current position
def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    lat_err = iss_latitude - MY_LAT
    lng_err = iss_longitude - MY_LONG
    if (-5.0 < lat_err < 5.0) and (-5.0 < lng_err < 5.0):
        print("ISS is close")
        return True
    else:
        print("ISS is not Nearby")
        return False

# and it is currently dark
def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    # Used GMT location +6
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 6
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 6
    if (time_now > sunset) or (time_now < sunrise) :
        print("this is night")
        return True
    else:
        return False

# Then send me an email to tell me to look up.
# Order matters: if one is false rest is not executed
# "if (is_dark() and iss_close()):" or "if (iss_close() and is_dark()):"
while True:
    time.sleep(10)
    time_now = datetime.now().hour
    if (is_dark() and iss_close()):
        with smtplib.SMTP("smtp.gmail.com") as sender:
            sender.starttls()
            sender.login(user= My_email, password= My_pw)
            sender.sendmail(from_addr= My_email, 
                            to_addrs= My_email, 
                            msg = "Subject: Int. Space Station Aleart !!!\n\n Yo!! Look at the sky Int. Space Station is nearby")

# BONUS: run the code every 60 seconds.


# python iss_overhead.py
