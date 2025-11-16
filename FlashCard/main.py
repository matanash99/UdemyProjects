import random
from tkinter import *
import time
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv", encoding='utf-8')
except FileNotFoundError:
    original_data = pd.read_csv("data/hebrew_words.csv", encoding='utf-8')
    data_dict = original_data.to_dict(orient= "records")
else:
    data_dict = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(language, text="English", fill= "black")
    canvas.itemconfig(word, text= current_card["English"], fill= "black")
    canvas.itemconfig(card_background, image= card_front_image)
    flip_timer = window.after(3000, func=flip)

def flip():
    canvas.itemconfig(language, text = "עברית", fill= "white")
    canvas.itemconfig(word, text= current_card["Hebrew"], fill= "white")
    canvas.itemconfig(card_background, image= card_back_image)

def know_card():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()





window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)
flip_timer = window.after(3000,func= flip)

canvas = Canvas(width= 800, height= 526)


# Load images
card_back_image = PhotoImage(file="C:/Udemy/Projects/FlashCard/images/card_back.png")
card_front_image = PhotoImage(file="C:/Udemy/Projects/FlashCard/images/card_front.png")
x_image = PhotoImage(file="C:/Udemy/Projects/FlashCard/images/wrong.png")
v_image = PhotoImage(file="C:/Udemy/Projects/FlashCard/images/right.png")


card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row= 0, column= 0, columnspan= 2)
language = canvas.create_text(400, 150, text= "", font= ("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text= "", font=("Ariel", 60, "bold"))

x_button = Button(image=x_image, highlightthickness=0, command= next_card)
x_button.grid(row= 1, column = 0)

v_button = Button(image=v_image, highlightthickness=0, command= know_card)
v_button.grid(row= 1, column = 1)


next_card()
window.mainloop()
#######################################################

# import random
# from tkinter import *
# import pandas as pd
# import os
# import sys
#
# BACKGROUND_COLOR = "#B1DDC6"
# current_card = {}
#
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)
#
# DATA_PATH = resource_path(os.path.join("data", "words_to_learn.csv"))
# ORIGINAL_DATA_PATH = resource_path(os.path.join("data", "hebrew_words.csv"))
#
# try:
#     data = pd.read_csv(DATA_PATH, encoding='utf-8')
# except FileNotFoundError:
#     original_data = pd.read_csv(ORIGINAL_DATA_PATH, encoding='utf-8')
#     data_dict = original_data.to_dict(orient="records")
# else:
#     data_dict = data.to_dict(orient="records")
#
# def next_card():
#     global current_card, flip_timer
#
#     window.after_cancel(flip_timer)
#     current_card = random.choice(data_dict)
#     canvas.itemconfig(language, text="English", fill="black")
#     canvas.itemconfig(word, text=current_card["English"], fill="black")
#     canvas.itemconfig(card_background, image=card_front_image)
#     flip_timer = window.after(3000, func=flip)
#
# def flip():
#     canvas.itemconfig(language, text="עברית", fill="white")
#     canvas.itemconfig(word, text=current_card["Hebrew"], fill="white")
#     canvas.itemconfig(card_background, image=card_back_image)
#
# def know_card():
#     data_dict.remove(current_card)
#     data = pd.DataFrame(data_dict)
#     data.to_csv(DATA_PATH, index=False)
#     next_card()
#
# window = Tk()
# window.title("Flashcard App")
# window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
# flip_timer = window.after(3000, func=flip)
#
# canvas = Canvas(width=800, height=526)
#
# card_back_image = PhotoImage(file=resource_path(os.path.join("images", "card_back.png")))
# card_front_image = PhotoImage(file=resource_path(os.path.join("images", "card_front.png")))
# x_image = PhotoImage(file=resource_path(os.path.join("images", "wrong.png")))
# v_image = PhotoImage(file=resource_path(os.path.join("images", "right.png")))
#
# card_background = canvas.create_image(400, 263, image=card_front_image)
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)
# language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
# word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
#
# x_button = Button(image=x_image, highlightthickness=0, command=next_card)
# x_button.grid(row=1, column=0)
#
# v_button = Button(image=v_image, highlightthickness=0, command=know_card)
# v_button.grid(row=1, column=1)
#
# next_card()
# window.mainloop()
#################################

