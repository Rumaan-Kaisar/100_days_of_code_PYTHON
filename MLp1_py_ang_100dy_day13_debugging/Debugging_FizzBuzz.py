# ----------------------  DEBUGGING ------------------------
# Noticce "or" is used insted of "and" in first condition
# also notice elif not used. So number is printed along with "fizz-buzz"
"""
for number in range(1, 101): 
  if number % 3 == 0 or number % 5 == 0 :
    print("FizzBuzz") 
  if number % 3 == 0: 
    print("Fizz") 
  if number % 5 == 0: 
    print("Buzz") 
  else:
    print([number])

"""
for number in range(1, 101): 
  if (number % 3 == 0) and (number % 5 == 0) :
    print("FizzBuzz") 
  elif number % 3 == 0: 
    print("Fizz") 
  elif number % 5 == 0: 
    print("Buzz") 
  else:
    print(number)

# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.

# python Debugging_FizzBuzz.py