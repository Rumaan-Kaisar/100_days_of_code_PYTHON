
travel_log_3 = [
  { "country":"France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
    "total_visited": 15},
  { "country": "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgrad"], 
    "total_visited": 5}
]


def add_new_country(countryName, no_visit, city_list):
  temp_dict = {}
  temp_dict["country"] = countryName
  temp_dict["cities_visited"] = city_list
  temp_dict["total_visited"] = no_visit
  travel_log_3.append(temp_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 20, ["Mumbai", "Gujrat", "Calcutta"])
print(travel_log_3)



# python nesting_excercise.py