PLACEHLDR = "[name]"

# reading names and store it as a list
with open("./Input/Names/invited_names.txt") as invited_peple_file:
    names = invited_peple_file.readlines() # returns the whole doc as list of lines with "\n"

with open("./Input/Letters/starting_letter.docx") as letter_unedited:
    content = letter_unedited.read() # returns the whole doc as a string
    
    # stripping a name and insert it in the content 
    for name in names:
        stripped_name = name.strip()
        letter_content = content.replace(PLACEHLDR, stripped_name)
        with open(file = f"./Output/ReadyToSend/send_to_{stripped_name }.docx", mode= "w") as edit_letter:
            edit_letter.write(letter_content)

# python main_soln_instr.py