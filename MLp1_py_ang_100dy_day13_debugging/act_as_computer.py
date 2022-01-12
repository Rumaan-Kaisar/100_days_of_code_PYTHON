# ----------------------  DEBUGGING ------------------------

# let's say input year is 1994, it deosn't belong to any of the condition.
# if you put it in a if statement, 1994>1980 ? => True, 1994 >1994 ? => False, True and False => Flase

# in following code 1994 doesnt print any thing
  # the reason is : 1994 is excluded accidentaly in the conditions.
  # if or elif both conditions does not includes 1994.
  # Solution is include 1994 in any one of those two conditions. Eg: <= 1994
"""
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

"""

year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# python act_as_computer.py