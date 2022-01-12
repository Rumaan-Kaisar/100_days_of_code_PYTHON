# following art comes form ASCII art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("you are at cross road. Where you wanna go? Left or Right? \n")

if direction.lower() == "left":
    path = input("There is a pond. How do you wanna go? Swim or Wait? \n")
    if path.lower() == "wait":
        boat = input("There is a Boat coming. wanna Ride? Y or N? \n")
        if boat.lower() == "y":
            door = input("Boat reached to Island. There are three doors: Red, Yellow and Blue? Which door ? \n")
            if door.lower() == "yellow":
                print("You win !! The box is found")
            elif door.lower() == "red":
                print("You Dead !! Eaten by mouse")
            else:
                print("Game over !! Boby Trap !!!!")
        else :
            print("Game over !! Earth quack quack !!!!")
    else:
        print("Dead !! Eaten by Aligator")
else:
    print("Game over !! Killed by Dainosour !!!!")

# if direction == "left" or direction == "Left":
#   action = input("Would you like to swim or wait?\n")
#   if action == "wait" or action == "Wait":
#     door = input("Which door? Red, Blue, or Yellow?\n")
#     if door == "red" or door == "Red":
#       print("Burned by fire. Game Over")
#     elif door  == "blue" or door == "Blue":
#       print("Eaten by beasts. Game Over")
#     elif door == "yellow" or door == "Yellow":
#       print("you win!!!!!!")
#     else:
#       print("Game Over!")
#   else:
#     print("attacked by trout.Game Over")
# else:
#   print("Fall into a hole! Game Over")