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

# The dealer gives the other person one card up and one card down, then the same for themselves. Now they look at their bottom card and add the face value to the top card. If you are about ten or less from twenty-one then you want to hit(get another card), If you are close to twenty-one you want to stay(keep the cards you have). If you break(go over) 21 then you have busted, this means that you are outfor the rest of this hand.
# Hit definition- when you want to get another card to get closer to 21, you can hit as many times as you want without going over 21.
# Stay definition- when you want to keep the same cards you
# have because you are confident you will beat your opponents hand, or you will bust if you hit.
# Bust definition- when the sum of your cards value is over 21 and you have to stop for that hand, and your opponent wins the hand because you bust.
# FACE VALUES:
# Ace-either one or eleven(the players choice)
# Two-2
# three-3
# Four-4
# Five-5
# Six-6
# Seven-7
# Eight-8
# Nine-9
# Ten-10
# Jack-10
# Queen-10
# King-10
# That is the face value for every card.


import art_blacK_Jack
import random

print(art_blacK_Jack.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)

# Extreme case
# plyr_card = [11, 11]
# pc_card = [11, 11]

plyr_card = [draw_card(), draw_card()]
pc_card = [draw_card(), draw_card()]


def total(plr_crd):
    plr_total = 0
    for crd in plr_crd:
        plr_total += crd

    if (11 in plr_crd):
        if plr_total > 21:
            print(f"index of 11 : {plr_crd.index(11)}")
            plr_crd[plr_crd.index(11)] = 1
            plr_total -= 10
            print(f"Place of 11 , replaced by 1 now : {plr_crd}")


    return plr_total



print(f"player cards : {plyr_card} and total = {total(plr_crd = plyr_card)}")
print(f"pC cards : {pc_card} and total = {total(plr_crd = pc_card)}")

def pc_dicision():
    if (total(pc_card) < 21) and (11 not in pc_card):
        dCsn = random.choice(["S", "H"])
        if dCsn == "H":
            hit2 = draw_card()
            pc_card.append(hit2)
    elif (total(pc_card) < 21) and (11 in pc_card):
        if  total(pc_card) > 21:
            print(f"index of 11 : {pc_card.index(11)}")
            pc_card[pc_card.index(11)] = 1
            print(f"Place of 11 , replaced by 1 now : {pc_card}")
        
        dCsn = random.choice(["S", "H"])
        if dCsn == "H":
            hit2 = draw_card()
            pc_card.append(hit2)


def ask():
    aSk = input("Want \"Hit\" or \"Stay\" or \"Call\"? Input 'H' or 'S' 'C'")
    if aSk == "H":
        hit = draw_card()
        plyr_card.append(hit)
        print(plyr_card)
        pc_dicision()
        ask()
    elif aSk == "S":
        pc_dicision()
        ask()
    elif aSk == "C":
        print("Game over")
        print(f"player cards : {plyr_card} and total = {total(plr_crd = plyr_card)}")
        print(f"pC cards : {pc_card} and total = {total(plr_crd = pc_card)}")
        if total(pc_card) == total(plyr_card):
            print("Draw")
        elif (total(pc_card) < total(plyr_card) <= 21):
            print("You win")
        elif total(plyr_card) > 21 >= total(pc_card):
            print("You are Busted. PC wins ")
        elif total(plyr_card) < total(pc_card) <= 21:
            print("PC wins ")
        elif (total(pc_card) > 21) and  (total(plyr_card) > 21):
            print("Draw")
        elif (total(plyr_card) <= 21 < total(pc_card)):
            print("You win")

ask()


# python blacK_Jack.py