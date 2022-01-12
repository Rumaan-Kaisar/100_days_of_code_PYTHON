# Don’t change the code below 
print("Welcome to the Love Calculator!") 
name1 = input("What is your name? \n") 
name2 = input("What is their name? \n")
# Don't change the code above
#Write your code below this line ^

# lower case conversion method
nam = (name1 + name2).lower()

# Letter counting

t = nam.count("t")
r = nam.count("r")
u = nam.count("u")
e = nam.count("e")
sum1 = str(t+r+u+e)

l = nam.count("l")
o = nam.count("o")
v = nam.count("v")
e = nam.count("e")
sum2 = str(l+o+v+e)

# we cannot compare string with int, so typecast needed
score = int(sum1 + sum2)

# Notice the modulo operator
if (10 > score) or (score > 90) : 
    print(f"\t\t Your score is {score}, You go togather like COKE and MENTOS \n\n")
elif (40 < score < 50 ):
    print(f"\t\t Your score is {score}, You are alrihgt togather \n\n")
else:
    print(f"\t\t Your score is {score}.")