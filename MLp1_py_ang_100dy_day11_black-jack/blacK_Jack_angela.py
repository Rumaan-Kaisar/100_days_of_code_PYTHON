# # # # # # # # # # # # # # #  Our Blackjack House Rules # # # # # # # # # # # # # # # # #

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

# # # # # # # # # # # # # # # # # # # # #  Hints # # # # # # # # # # # # # # # # # # # # #




import art_blacK_Jack
import random
import os


# ---------------- Randomly deal cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card



# ---------------- Create a function called compare() and pass in the user_score and computer_score:
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses. 
    # If the user has a blackjack (0), then the user wins. 
    # If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses. 
    # If none of the above, then the player with the highest score wins.



def compare(u_sCr, pc_ScR):
    if u_sCr == pc_ScR:
        return f"Draw"
    elif u_sCr == 0:
        return f"User wins"
    elif (pc_ScR == 0):
        return f"Pc wins"
    elif pc_ScR > 21:
        return f"User wins !!! PC busted"
    elif u_sCr > 21:
        return f"Pc wins !!! User busted"
    elif pc_ScR > u_sCr:
        return f"Pc wins"
    elif pc_ScR < u_sCr:
        return f"You win !!"



# ---------------- Calculate score: 
    #  Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    #  Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
def calculate_score(cRDs):
    """ Take a list of cards and return the score calculated from the cards """
    if (sum(cRDs) == 21) and (len(cRDs) == 2):
        return 0

    if (sum(cRDs) > 21) and (11 in cRDs):
        cRDs.append(1)
        cRDs.remove(11)

    return sum(cRDs)



# ---------------- The main function
def blackjack_main():

    print(art_blacK_Jack.logo)
    
    # DEal the cards: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    pc_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends
    # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print(f"Your cards : {user_cards} and total = {user_score}")
        print(f"Pc's first card : {pc_cards[0]} ")

        if (user_score == 0) or (pc_score == 0) or (user_score > 21):
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # PC choice: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while 0 < pc_score < 17 :
        pc_cards.append(deal_card())
        pc_score = calculate_score(pc_cards)


    print(f"Your final hand : {user_cards} and Final Score = {user_score}")
    print(f"PC's final hand : {pc_cards} and Final Score = {pc_score}")
    print(compare(user_score, pc_score))



# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input(f"Wanna paly again? Press y if yes: ") == 'y':
    os.system("cls")
    blackjack_main()


# python blacK_Jack_angela.py