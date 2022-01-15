
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
#  Don't change code above 

# Write your code  below:
weather_f = {day:(cel*(9/5)) + 32 for (day, cel) in weather_c.items()}
print(weather_f)


# python frnh_cel_dic_cmph.py