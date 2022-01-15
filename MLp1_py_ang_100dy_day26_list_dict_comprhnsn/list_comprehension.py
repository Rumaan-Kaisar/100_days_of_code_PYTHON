# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = [len(item) for item in fruits]
# print(new_list)


# conditional List comprehension
# a_in_fruits_list = [item for item in fruits if ("a" in item)]

# newlist = [x for x in fruits if x != "apple"]

# newlist = [x for x in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# newlist = [x for x in range(10)]

# newlist = [x for x in range(10) if x < 5]

# print(a_in_fruits_list)
# print(newlist)


# ------------  Examples:  -------------
# --------------   apply to numbers   ---------------
numbers = [1, 2, 3]
new_numbers = [i+ 1 for i in numbers]
print(new_numbers)


# --------------   apply to strings   ---------------
name = "Bandhu"
letters_on_name = [ch for ch in name]
print(letters_on_name)


# --------------   working with range   ---------------
dubled = [2*i for i in range(1, 5)]
print(dubled)

# --------------   apply to strings   ---------------
#only add names have four letters. Filter the names
# in this case, new_item and item's name are same; because we just want a list of items that's passed the condition.

names = ['Alex', 'Beth', 'Caroline', 'Eleanor' ]
four_letter_names = [item for item in names if (len(item) == 4)]
print(four_letter_names)

# Above names in uppercase
upper_case_names = [nm.upper() for nm in names]
print(upper_case_names)

# python list_comprehension.py