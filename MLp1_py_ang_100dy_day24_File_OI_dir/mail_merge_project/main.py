#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Create name-list from the  invited_names.txt
names_file = open(file="./Input/Names/invited_names.txt", mode="r")
name_list = names_file.readlines()
names_file.close()

# Read starting_letter.docx
letter_line_file = open(file="./Input/Letters/starting_letter.docx", mode="r")
line_list = letter_line_file.readlines()
letter_line_file.close()

#  stripping the names
names = []

for i in range(0, len(name_list)):
    if name_list[i] == "\n":
        pass
    else:
        nme = name_list[i].strip("\n")
        names.append(nme)


# writting the letters
for j in range(0, len(names)):
    line_1 = line_list[0]
    first_line = line_1.replace("[name]", names[j])
    write_string = ""
    write_string += first_line
    for k in range(1, len(line_list)):
        write_string += line_list[k]
    # print("\n", write_string)
    write_file = open(file = f"./Output/ReadyToSend/{names[j]}.docx", mode="w")
    write_file.write(write_string)
    write_file.close()
    

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# python main.py