import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))


# Converting DataFrame to dictionary
data_dict = data.to_dict()
print(data_dict)

# Converting Series to list
temp_list = data["temp"].to_list()
print(temp_list)

# -------- Average Temperatue : Using built-in Python methods "sum" ---------
average = sum(temp_list)/len(temp_list)
print(f"Average Temperatue : Using built-in Python method is   : {average}")

# -------- Average Temperatue : Using built-in PANDAS method: mean(), median(), mode(), max() etc---------
average_pandas = data["temp"].mean()
print(f"Average Temp : Using built-in PANDAS method   : {average_pandas}")

max_value = data["temp"].max()
print(f"Max Temp : Using built-in PANDAS method   : {max_value}")

# Get data in COLUMNS: the string must match to the column-title
print(data["condition"]) # treat as a "Dictionary"
print(data.condition)  #  treat as an "Object": Alternative way

# Get data in ROWS: Notice all [] arew used. First with DataFrame then with Series
# Notice the conditional statement
print(data[data["day"] == "Monday"])

# Print day with maximum teperature
print(data[data["temp"] == data["temp"].max()])
# or Equivalently
print(data[data.temp == data.temp.max()])

# Accessing particular/specific data from a ROW
mnday = data[data.day == "Monday"]
print(mnday.condition)

#temperature Cel to Ferh
mnday_temp = int(data[data.day == "Monday"].temp)
print(mnday_temp*100)
# or Equivalently
temp_of_mon = int(mnday.temp)
ferenheit = (temp_of_mon * (9/5)) + 32
print(ferenheit)



# Create a Dataframe/CSV from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"], 
    "scores": [76, 56, 65]
}

created_dt_frm = pandas.DataFrame(data_dict) # this creates the Dataframe
print(created_dt_frm)
created_dt_frm.to_csv("created_dt_frm.csv") # This converts to CSV

# More on numPy , Matplotlib and others

# python more_panda_opr.py