nUm = int(input("Enter the terminal value : "))

for x in range(1, nUm+1):
    if (x % 3)  == 0 : 
        if (x % 5) == 0 :
            print("FizzBuzzz")
        print("Fizz")
    elif (x % 5) == 0 :
            print("Buzzz")
    else:
        print(x)

# Other way
print("\n\n\nOther way\n")
for y in range(1, nUm+1):
    if ((y % 3)  == 0) and ((y % 5)  == 0):
        print("FizzBuzzz")
    elif (y % 3)  == 0 : 
        print("Fizz")
    elif (y % 5) == 0 :
            print("Buzzz")
    else:
        print(y)

# python fizzbuzz.py