import random

# Rock Paper Scissors ASCII Art

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

user= int(input("Choose 1 for Rock, 2 for Scissor, 3 for Paper : "))

pc_rand = random.randint(1, 3)

element = [rock, scissors, paper]

if (user > 2) or (user < 0): 
    print("Invalid Number. PC wins")
elif pc_rand == user :
    print(f"\n\tYou Chosed :\n{element[user-1]}\n\n\tPC chosed :\n {element[pc_rand-1]}\n\n\t\tDRAW")
elif (pc_rand == 1) and (user == 2):
    print(f"\n\tYou Chosed :\n{element[user-1]}\n\n\tPC chosed :\n {element[pc_rand-1]}\n\n\t\tPC wins")
elif (pc_rand == 1) and (user == 3):
    print(f"\n\tYou Chosed :\n{element[user-1]}\n\n\tPC chosed :\n {element[pc_rand-1]}\n\n\t\tUser wins")
elif (pc_rand == 2) and (user == 1):
    print(f"\n\tYou Chosed :\n{element[user-1]}\n\n\tPC chosed :\n {element[pc_rand-1]}\n\n\t\tUser wins")
elif (pc_rand == 2) and (user == 3):
    print(f"\n\tYou Chosed :\n{element[user-1]}\n\n\tPC chosed :\n {element[pc_rand-1]}\n\n\t\tPC wins")
elif (pc_rand == 3) and (user == 2):
    print(f"\n\tYou Chosed :\n{element[user-1]}\n\n\tPC chosed :\n {element[pc_rand-1]}\n\n\t\tUser wins")
elif (pc_rand == 3) and (user == 1):
    print(f"\n\tYou Chosed :\n{element[user-1]}\n\n\tPC chosed :\n {element[pc_rand-1]}\n\n\t\tPC wins")
# python rc_pap_sci.py
