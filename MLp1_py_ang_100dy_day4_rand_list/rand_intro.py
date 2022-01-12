import random

# Integer random: following generate random int between 1 and 10
random_int = random.randint(1, 10)
print(f"int random number between 1 to 10 is : {random_int}")

# Float random: following generate random float between 0 and 1 i.e (0, 1)
random_float = random.random()
print(f"float random number between 0 to 1 is : {random_float}")

#follwoing gives float randoms betwwen 0 and 4
print(f"random number between 0 to 5 is : {random.random()*5}")


# Modified Love calculator: Generates random number from 1 to 100
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# python rand_intro.py