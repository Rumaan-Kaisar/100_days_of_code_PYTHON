import random

data = input("Enter the names : ")

# splitting string
names = data.split(", ")
print(f"Your data is: {names}")

# length = len(names)
# ran = random.randint(1, length)

# using random.choice
ran_name = random.choice(names)

print(ran_name + "Will pay the bill today")
# python bnkrulet.py

#Nested lists
fruit = ["Cherry", "Apple", "Pear"]
veg = ["Potato", "Tomato", "Carrot"]

# following is nested list
buy_list = [fruit, veg]
print(buy_list)

# Output: [['Cherry', 'Apple', 'Pear'], ['Potato', 'Tomato', 'Carrot']]