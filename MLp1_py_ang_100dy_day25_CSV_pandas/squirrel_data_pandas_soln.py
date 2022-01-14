import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

# Acess the rows and count them
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

result = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinamon, black]
}

result_csv = pandas.DataFrame(result)
print(result_csv)
result_csv.to_csv("Squirrel_color_count.csv")

# python squirrel_data_pandas_soln.py