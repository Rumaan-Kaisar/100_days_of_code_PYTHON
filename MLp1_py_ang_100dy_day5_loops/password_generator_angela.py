# Password generator project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ======   Easy level  ======
creating string of random characters
passWord = ''
for char in range(1, nr_letters + 1):
    # randomly choose letters and add to string
    passWord += random.choice(letters)

for char in range(1, nr_symbols + 1):
    passWord += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    passWord += random.choice(numbers)

print("\n\t\tEasy Level password : ", passWord)



# ======     Hard level    ========
passWord_list = []
for char in range(1, nr_letters + 1):
    # randomly choose letters and add to string
    passWord_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    passWord_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    passWord_list.append(random.choice(numbers))

print(passWord_list)

random.shuffle(passWord_list)

print(passWord_list)

# creating final password string
paswrd = ''
for i in passWord_list :
    paswrd += i

print(f"\n\n\t\tPassword is : {paswrd} \n")


# python password_generator_angela.py