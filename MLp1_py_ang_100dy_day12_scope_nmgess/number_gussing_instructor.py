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


from random import randint

# generate random number

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
  """ chekcs answer against guess, returns the number of turns remaining """
  if guess == answer:  
    print(f"Congrats. Answer was {answer}")
    if input("restart? y or n: ") == "y":
      game()
    return
  elif guess > answer:
    print("Too high")
    return turns -1 # before, I used += which is bound to variable 
  elif guess < answer:
    print("Too low")
    return turns -1

#set difficulty and attempts
def difficulty():
  level = input("Choose a difficulty. easy or hard?: ")
  # in this stage, creating global constants
     # if I create variable'turns' using =, inside function,  it's no use as it's local, 
     # instead, use "return" so I can use it whenever I call this function:  set global var and assign the function to get output.
  if level == "easy":
    return EASY_LEVEL
    print("10 attempts")
  else:
    return HARD_LEVEL 
    print("5 attempts")


def game():
  answer = randint(1, 100)

  print("welcome")
#   print(answer)
  #loop user guess - compare - result if they get it wrong. if get it right, finish.
  
  turns = difficulty() 
  # setting local variable turns,output of difficult() is EASY_LEVEL OR HARD_LEVEL  which contains 10, 5 each and it's number of turns.

  guess = 0 
  # when creating while loop, guess is defined after while, so make an empty one first. it will be only used once.
  
  while guess != answer and turns != 0:
  	#get user guess 
    print(f"you have {turns} attempts remaining to guess the number.")
    guess = int(input("Guess a number btw 1 to 100: "))
    
    # compare guess with answer #show result
    # track thenumber of turns, reduce by 1 if they get it wrong 
   
    turns = check_answer(guess, answer, turns) # check_answer returns output: turns -1 . Also prints direction   
    
    if turns == 0:
      print("you've run out of guess the number")
      if input("restart? y or n: ") == "y":
        game()
      return # 🚨 to exit and end function
    
game()

# python number_gussing_instructor.py
