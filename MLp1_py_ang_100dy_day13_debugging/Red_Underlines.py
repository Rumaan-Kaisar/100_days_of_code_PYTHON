# ----------------------  DEBUGGING ------------------------

# 1. notice the underline in editor; Expecting indent
# 2. also type-coversion is needed. Somtimes googling error messges works.
        # Use "stackoverflow"
# 3. Fixing above will works perfectly, But also there is a bug. Notice "f" missing in f-string



"""
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

"""

age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# python Red_Underlines.py