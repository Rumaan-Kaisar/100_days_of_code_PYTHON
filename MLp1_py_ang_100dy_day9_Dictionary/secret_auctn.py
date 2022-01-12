import secret_auctn_art
import os

print(secret_auctn_art.logo)
print("WelCome to secret Auction")

bids = {}

end = False

while not end:
  name = input("\n\tEnter your name : ")
  price = int(input("\n\tWhat is your bid-value? $ : "))
  bids[name] = price
  
  ask = input("Are there any other bidders? Type 'yes' or 'no' : ")
  if ask == "yes":
    # clear screen
    os.system('cls')
  elif ask == "no":
    print(bids)
    print("\n\t\t\tgoodbye\n")
    end = True


mAx = 0
winner = ""

for bidder in bids:
  if bids[bidder] > mAx:
    mAx = bids[bidder]
    winner = bidder

print(f"\n\t\t The winner is : {winner} with Amount {mAx}\n")

# python secret_auctn.py