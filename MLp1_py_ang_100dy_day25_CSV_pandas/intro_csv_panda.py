
# No library: Accessing CSV file data, without using any library
with open(file= "weather_data.csv", mode="r") as weather_data:
    day_list = weather_data.readlines()

print(day_list)



# CSV python-library: Accessing CSV file data, with default CSV python-library
import csv

temparatures = []

with open(file= "weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    for dt in data:
        print(dt)
        if dt[1] != "temp":
            temparatures.append(int(dt[1]))
    
print(temparatures)


# PANDAS: Accessing CSV file data, with PANDAS library.
import pandas

data_2 = pandas.read_csv("weather_data.csv")
print(data_2)

# printing temperature: Easyly with pandas
print(data_2["temp"])

# python intro_csv_panda.py