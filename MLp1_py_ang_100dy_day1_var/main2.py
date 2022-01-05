# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the" + " + sign.")
# print("e.g. print('Hello ' + 'world')") 
# print("New lines can be created with a backslash and n.")

# print(len(input("Your name ? ")))

name = input("What is your name ? ")
print("Hello " + name)
name_length = len(name)
# to concatenate length of name must be a string. So str() is used
print( "Length of " + name + " is = " + str(name_length) )