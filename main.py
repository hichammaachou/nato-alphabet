
import pandas

#Loop through rows of a data frame


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input('name: ')
name_list = [nato_alphabet_dict[l.upper()] for l in name if l.upper()== nato_alphabet_dict[l.upper()][0]]
print(name_list)
