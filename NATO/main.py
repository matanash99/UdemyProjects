import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}
print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():

    user_word = input("Enter a word and I will show you the NATO representation: ").upper()
    try:
        nato_result = [nato_dict[letter] for letter in user_word]

    except KeyError:
        print("Wrong key enter letters only")
        generate_phonetic()
    else:
        print(nato_result)


generate_phonetic()