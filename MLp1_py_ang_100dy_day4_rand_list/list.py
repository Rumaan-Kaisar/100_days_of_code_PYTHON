# List is a Data Structure in Python
# It stores list of data as : [otem1, item2, . . . ]. 
# It is used for Grouping and Ordering data

fruits = ["Cherry", "Apple", "Pear"]

#the items vcan be accessed/modified just like array.
print(fruits[2])
fruits[2] = "Havana"
print(fruits[2])

# You can also use negative index. To access items from the END
# "-1" indicates last item. So no "-0"
print(fruits[-1])


# Adding new items. Index doesn't matter
fruits.append("Jackfruit")
print(fruits[-1])

#Extending list
fruits.extend(["Mango", "Banana", "Pineapple"])
print(fruits)