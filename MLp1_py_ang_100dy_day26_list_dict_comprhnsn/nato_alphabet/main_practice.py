
import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

name = input("Enter the name :").upper()
list_of_letters = name.strip()

dictionary_of_name_latters = {row.letter: row.code for (idx, row) in nato_data.iterrows() if (row.letter in list_of_letters)}

list_of_code = [dictionary_of_name_latters[ch] for ch in list_of_letters]

print(dictionary_of_name_latters)
print(list_of_code)


# python main.py