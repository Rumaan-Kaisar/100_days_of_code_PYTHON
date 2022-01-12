# Password generator project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

lTr = len(letters)-1
sYm = len(symbols)-1
nMr = len(numbers)-1

# creating string of random characters
pw = ''
for i in range(0, nr_letters):
    pw += letters[random.randint(0, lTr)]

for i in range(0, nr_symbols):
    pw += symbols[random.randint(0, sYm)]

for i in range(0, nr_numbers):
    pw += numbers[random.randint(0, nMr)]

print("\t\t Un-suffled final Password  : ", pw)


# ========== Suffling the characters ==========
if len(pw) > 0 :
    sUfl = [pw[0]]

    # Creating list of password characters
    for i in range(1, len(pw)) :
        sUfl.append(pw[i])

    print("\n\n\t\t List of password characters  Before suffle : ",sUfl)

    # suffling
    random.shuffle(sUfl)

    # creating final password string
    paswrd = ''

    for i in range(0, len(sUfl)) :
        paswrd += sUfl[i]

    # random.shuffle(sUfl) itself nothing; just changes the given list. 
    # so print("suffoled : ", random.shuffle(sUfl)) not applicable
    print("\n\t\tsuffoled password characters : ", sUfl)
    print("\n\t\tFinal Password : ", paswrd)
    print("\n\t\tLength Password : ", len(paswrd))


# python password_generator.py