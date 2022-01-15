
import pandas

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# data_dict = {
#     "students": ["Amy", "James", "Angela"], 
#     "scores": [76, 56, 65]
# }

# looping through Dictionary
for (day, temp) in weather_c.items():
    print(f"Day : {day} , Temp : {temp}\n")

# dictionary to list. "Scaler" to "vector"
weather_data = {
    "day": [dAy for (dAy, teMp) in weather_c.items()],
    "temp": [teMp for (dAy, teMp) in weather_c.items()]
}

weather_data_frme = pandas.DataFrame(weather_data)

print(weather_data_frme)

# Gives titles of each columns 
for (key, value) in weather_data_frme.items():
    print(key) # Gives titles of each columns 
    print(value) # Gives  column values

# --------------    iterrows() --------------
# the iterrows() helps to loop through rows of data frame
for (inDex, rOw) in weather_data_frme.iterrows():
    # print(inDex)
    # print(rOw)
    # Accessing specific row
    print(rOw.temp) # shows temperature
    # print(rOw.day) # shows dayes
    if rOw.day == "Friday":
        print(rOw.temp)


# python lopp_panda_dataframe.py