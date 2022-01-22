import requests
import datetime as dTm

# Moscow is used
My_Lat = 55.7558
My_long = 37.6173

# this Dictionary needs to contain exact keya wich are the params of API
# "formatted" :0, Used for 24-hour format
poStn = {
    "lat" : My_Lat,
    "lng" : My_long,
    "formatted" :0
}

sun_resp = requests.get(url = "https://api.sunrise-sunset.org/json", params= poStn)
sunrise_data = sun_resp.json()

sun_rise_row = sunrise_data["results"]["sunrise"]
sun_set_row = sunrise_data["results"]["sunset"]

# splitting and grabbing the hour only from -- 2022-01-22T05:37:50+00:00, 
# seperating "05"
sun_rise_hour = sun_rise_row.split("T")[1].split(":")[0]
sun_set_hour = sun_set_row.split("T")[1].split(":")[0]

# acessing PC current hour. Above is done for comare to following
pc_hour = dTm.datetime.now().hour

print(f"sun_rise_hour :{sun_rise_hour},  sun_set_hour :{sun_set_hour}, And pc_hour : {pc_hour}")

# python api_params.py
