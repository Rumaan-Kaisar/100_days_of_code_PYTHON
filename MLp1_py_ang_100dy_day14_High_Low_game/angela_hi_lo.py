from celeb_data import data
import random
from hi_lo_art import logo, vs
import os

# Display art.
print(logo)

score = 0 

game_should_continue = True




# Format account data into printable format.

def format_data(acuNt):
    """Format account into printable format: name, description and country"""
    name = acuNt["name"]
    description = acuNt["description"]
    country = acuNt["country"]
    return f"{name}, a {description}, from {country}"

# compare the data
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    # if (a_followers > b_followers) and (guess == "a"):
    #     return True
    # elif (b_followers > a_followers) and (guess == "b"):
    #     return True
    # else:
    #     return False

    # Shorter version is using "conditional return". Indirect "True" or "False"
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Follwing is just for first step/iteration/startup and for first shuffle 
# Act as "step -1" and never touched when "while" loop runs
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data.

    # following is the actual shuffle
        # first "account_b" outside of "while" will never executed when this loop continues
    account_a = account_b #stores previous steps "account_b" 
    #Generates new "account_b" for Current step and will be next "account_a" in follwing step
    account_b = random.choice(data) 

    while account_a == account_b:
        account_b = random.choice(data)

    # Make B become the next A.

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    # Check if user is correct.
        ## Get follower count.
        ## If Statement

    folllower_a = account_a["follower_count"]
    folllower_b = account_b["follower_count"]

    is_correct = check_answer(guess, folllower_a, folllower_b)

    os.system("cls")
    print(logo)

    # Give user Feedback on their guess.
    # Score Keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
    
      
# Make game repeatable.

# Display art.

# Clear screen between rounds.

# python angela_hi_lo.py

