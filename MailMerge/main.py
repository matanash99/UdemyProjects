#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from tkinter.font import names

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Input/Letters/starting_letter.txt", "r") as starting_file:
    before_replacement = starting_file.read()

with open("./Input/Names/invited_names.txt", "r") as name_file:
    invited_names = name_file.readlines()

for name in invited_names:
    current_name = name.strip()
    new_mail = before_replacement.replace("[name]",current_name)
    with open(f"./Output/ReadyToSend/letter_for_{current_name}.txt", "w") as current_mail:
        current_mail.write(new_mail)

