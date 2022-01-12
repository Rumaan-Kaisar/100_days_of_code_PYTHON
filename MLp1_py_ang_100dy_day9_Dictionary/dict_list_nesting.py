# Nesting list inside dictionary
carDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": [1964, 1890, 2008, 2509]
}

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgrad"]
}
print(carDict["year"])
print(travel_log["Germany"][2])
print(travel_log)


# Nesting list inside list
bui = ["a", "c", [1, 2, 5], "D"]
print(bui)
print(bui[2][1])


# Nesting Dictionary inside Dictionary
travel_log_2 = {
  "France": {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visited": 15},
  "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgrad"], "total_visited": 5}
}

print(travel_log_2["France"])
print(travel_log_2["France"]["cities_visited"])
print(travel_log_2["Germany"]["total_visited"])



# Nesting Dictionary inside List
travel_log_3 = [
  { "country":"France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
    "total_visited": 15},
  { "country": "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgrad"], 
    "total_visited": 5}
]

print(travel_log_3)
print(travel_log_3[1]["country"])
print(travel_log_3[0]["cities_visited"][2])


# python dict_list_nesting.py