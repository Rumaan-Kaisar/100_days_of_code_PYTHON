import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]

gray = 0
cinamon = 0
black = 0

for squrl_colr in fur_color:
    if squrl_colr == "Gray":
        gray += 1
    elif squrl_colr == "Cinnamon":
        cinamon += 1
    elif squrl_colr == "Black":
        black += 1

print(f"Gray : {gray}, Black {black}, Cinamon : {cinamon}")

result = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinamon, black]
}

result_csv = pandas.DataFrame(result)
print(result_csv)
result_csv.to_csv("Squirrel_fur_color_count.csv")

# python squirrel_data_pandas.py