
import requests

resPonse = requests.get(url = "http://api.open-notify.org/iss-now.json")
print(resPonse)
only_status_code = resPonse.status_code
print(only_status_code)


# specify exception
resPonse.raise_for_status()

# Accessing the data: Same way we are used to retrive from JSON
data = resPonse.json()
print(data)
print(data["iss_position"]["longitude"])
print(data["iss_position"]["latitude"])
coor_Dnitate = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
print(coor_Dnitate)




# python api_first_demo.py



    

    

    

