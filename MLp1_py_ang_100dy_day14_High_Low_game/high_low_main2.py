# import modules & random
import random
import hi_lo_art
import celeb_data
import os

# My style: Keep code as simple as possible. Don't use too much function for "abstruction"
ran_celeb1 = random.choice(celeb_data.data)

def game():
  global ran_celeb1
  # 1. Choose randomly 2nd persons data "dictionary" from the "list" of data
  ran_celeb2 = random.choice(celeb_data.data)

          # to prevent duplication
  while ran_celeb1["name"] == ran_celeb2["name"]:
    ran_celeb2 = random.choice(celeb_data.data)
    # n1 =ran_celeb1["name"]
    # n2 = ran_celeb2["name"]
    # print(f"celeb1 : {n1}    celeb2 : {n2}")

  name1 =ran_celeb1["name"]
  follower_count1 = ran_celeb1["follower_count"]
  description1 = ran_celeb1["description"]
  country1 = ran_celeb1["country"]

  name2 = ran_celeb2["name"]
  follower_count2 = ran_celeb2["follower_count"]
  description2 = ran_celeb2["description"]
  country2 = ran_celeb2["country"]


  # 2. Show logos and show celebrety data
      # Format message from dictionary
  print(hi_lo_art.logo)
  print(f"Compare A : {name1}, {description1}, from {country1}")
  print(hi_lo_art.vs)
  print(f"Compare B : {name2}, {description2}, from {country2}")


  # 3. Ask user to guess untill they get wrong
      # If right : continue and count score
      # If wrong : Show score

  ask = input(f"Who has more follower? Type 'A' or 'B'").lower()
  print(ask)

  if ask == "a":
    if follower_count1 > follower_count2:
      print("You are Right")
      # B becomes next A
      ran_celeb1 = ran_celeb2
      return True
    else:
      print("Soorrry you are wrong")
      return False
  elif ask == "b":
    if follower_count2 > follower_count1:
      print("You are Right")
      # B becomes next A
      ran_celeb1 = ran_celeb2
      return True
    else:
      print("Soorrry you are wrong")
      return False

cnTnu = True
score = 0
while cnTnu:
  cnTnu = game()
  if cnTnu == True:
    score += 1
    os.system("cls")

print(f"Your score is : {score}")

# python high_low_main2.py

