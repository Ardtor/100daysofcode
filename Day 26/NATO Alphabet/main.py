
import pandas as pd

# The below could be used if pandas wasn't a requirement of this lesson 
# import csv
# with open("data/nato_phonetic_alphabet.csv") as f:
#     nato_alphabet = {letter: word for letter, word in csv.reader(f)}

nato_alphabet = pd.read_csv("data/nato_phonetic_alphabet.csv")
# as a dataframe uses a index, it's unused as part of a simple key:value pair dictionary for this
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
user_input = input("Please enter a word: ").upper().replace(" ", "")
nato_words = [nato_alphabet[letter] for letter in user_input]
print(nato_words)
