import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (idx, row) in nato_data.iterrows()}

name = input("Enter the name :").upper()
list_of_code = [phonetic_dic[ch] for ch in name]
print(list_of_code)

# python main.py