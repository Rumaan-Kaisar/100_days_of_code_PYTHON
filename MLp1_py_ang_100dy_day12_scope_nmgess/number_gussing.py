#-----------------------------<My code>----------------------------
logo = """


  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               
"""

import random


def compare(usrNnum, rndNum):
    if usrNnum == rndNum:
        return "correct"
    elif (rndNum - 10) < usrNnum < (rndNum + 10):
        if (rndNum - 5) < usrNnum < (rndNum + 5):
            if usrNnum < rndNum :
                return f"Guess again a little bit higher."
            elif usrNnum > rndNum :
                return f"Guess again a little bit lower."

        else:
            if usrNnum < rndNum :
                return f"Guess a bit bigger number."
            elif usrNnum > rndNum :
                return f"Guess a bit smaller number."
    else:
        if usrNnum < rndNum :
                return f"too small"
        elif usrNnum > rndNum :
            return f"too big"



game_over = False

while not game_over:
    print(logo)
    rand_num = random.randint(1, 100)
    print("random number is", rand_num)

    ask = input("\n\t Want to play 'Hard' or 'Easy', input 'h'/'e' : ").lower()

    if ask == 'h':
        count = 5
    elif ask == 'e':
        count = 10
    else:
        print("Invalid char. Using easy mode")
        count = 10

    i = 0
    while (i < count):
        user_guess = int(input("Enter a Number between 1 to 100: "))
        if compare(user_guess, rand_num) != "correct":
            print("Chances left : ", count-1-i)
            print(compare(user_guess, rand_num))
            i += 1
        elif compare(user_guess, rand_num) == "correct":
            print("Well done!!!! you guessed the correct number!!!")
            i = count

    if input("Wanna play again ? y/n :") == 'n':
        game_over = True

# python number_gussing.py