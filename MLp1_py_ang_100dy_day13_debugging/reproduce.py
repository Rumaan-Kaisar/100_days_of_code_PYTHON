# ----------------------  DEBUGGING ------------------------

# Debug following by reproducing the bug
# from random import randint
# dice_imgs = ["A", "B", "C", "D", "E", "F"]
# dice_num = randint(1, 6)

# print(dice_imgs[dice_num])

# Using for loop to find the bug. Index out range will appear eventually
        # Traceback (most recent call last):
        #   File "reproduce.py", line 16, in <module>
        #     print(dice_imgs[dice_num])
        # IndexError: list index out of range

# Problems are : A doesn't appear, Index error appear. 
# Cahnge the rand int : randint(1, 6) to randint(0, 5)
"""
for i in range (0, 19):
  from random import randint
  dice_imgs = ["A", "B", "C", "D", "E", "F"]
  dice_num = randint(0, 5)

  print(dice_imgs[dice_num])
  
  """
  
from random import randint
dice_imgs = ["A", "B", "C", "D", "E", "F"]
dice_num = randint(0, 5)

print(dice_imgs[dice_num])

# python reproduce.py