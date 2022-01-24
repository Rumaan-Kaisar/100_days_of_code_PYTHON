import requests
import json

my_lat = 23.810331
my_lan = 90.412521

parAm = {
    "lat" : my_lat,
    "lon" : my_lan,
    # ignore/exclude the other data. No space used only ","
    "exclude" : "current,minutely,daily",
    "appid" : "-----"
}

dt_req = requests.get(url = "https://api.openweathermap.org/data/2.5/onecall", params= parAm)
dt_req.raise_for_status()
daTa = dt_req.json()
# print(daTa)

# save Data to a .json file
# with open("weather_data.json", "w") as data_file:
#     # Saving the new data. Notice "json module" is used
#     json.dump(daTa, data_file, indent=4)

# # read from Json
# with open("weather_data.json") as read_file:
#     json_data = json.load(read_file)

# # List-slicing: Lst[ Initial : End : IndexJump ]
# sliced_hour = json_data["hourly"][0 : 12 : 1]

bring_umbrla = False

sliced_hour = daTa["hourly"][0 : 12 : 1]

for hUr in sliced_hour:
    print(hUr)
    ids = hUr["weather"][0]["id"]
    print(ids)
    if 500 <= int(ids) < 532:
        bring_umbrla = True

if bring_umbrla:
    print("Bring Umbrella")



# python authn_api_demo.py