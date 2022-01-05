#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
# https://band-name-generator-end.appbrewery.repl.run/


print("\n\n -- Hi! Welcome to Band Generator -- \n\n")
print(" To generate The Band name, we need some info. \n \t Give answer to following questions :\n\n")
city = input(" 01 - Name the city that you grew up in : \n\t")
pet = input(" 02 - What is the name of your pet : \n\t")
print("\n\n your BAND name would be : '"+ pet +" "+  city + "'")