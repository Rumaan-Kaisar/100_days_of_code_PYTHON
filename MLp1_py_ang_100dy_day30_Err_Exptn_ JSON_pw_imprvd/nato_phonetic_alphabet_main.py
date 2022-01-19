# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def nato_aplhbt():
    word = input("Enter a word: ").upper()
    try :
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_aplhbt()
    else:
        print(output_list)

nato_aplhbt()

# python nato_phonetic_alphabet_main.py