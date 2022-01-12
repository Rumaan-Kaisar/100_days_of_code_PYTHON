# key - value pair

dictionary_test = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
    "Loop": "The action of doing something over and over again."
}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Retriving items from DIctionaries
# dictionary_name[key]

bug_data = dictionary_test["Bug"]
print(bug_data)

print(thisdict["year"])
print(thisdict)


#Adding new items to dictionary.
dictionary_test["Book"] = "Tings with papaer and ink"
print(dictionary_test)


#Create an empty dictionary.
new_dict_test = {}

#Wipe an existing dictionary
thisdict = {}
print(thisdict)


#Edit an item in a dictionary
dictionary_test["Book"] = "Edited Book"

# For loop of dictionary
for key in dictionary_test : 
    print(key)
    print(dictionary_test[key])

# python dict.py