#Don't change the code below

print("Welcome to Python Pizza Deliveries!")

print("\n\n\tSmall Pizza: $15 \n\tMedium Pizza: $20 \n\tLarge Pizza: $25")
print("\n\tPepperoni for Small Pizza: +$2 \n\tPepperoni for Medium or Large Pizza: +$3")
print("\n\tExtra cheese for any size pizza: + $1")

size = input("\n\nWhat size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# 3 Don't change the code above

# Write your code below this line

bil = 0

if size == "S" : 
    bill = 15
elif size == "M" : 
    bill = 20
elif  size == "L" : 
    bill = 25
else :
    print(f"\n\t Please Check again !! \n\n")

if add_pepperoni == 'Y':
    if size == "S" : 
        bill += 2
    else:
        bill += 3
    
if extra_cheese == 'Y':
    bill += 1

print(f"\n\t Your Bill is: ${bill}. Thank you. \n\n")