from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():

    password_entry.delete(0, END)
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

    numbers = [str(i) for i in range(10)]

    random_length = random.randint(8,12)
    generated = ""
    for i in range(random_length):
        random_one_eight = random.randint(1,8)
        if random_one_eight == 4 or random_one_eight == 5:
            generated += random.choice(symbols)
        elif random_one_eight == 6 or random_one_eight == 7:
            generated += random.choice(numbers)

        else:
            generated += random.choice(letters)

    pyperclip.copy(generated)
    password_entry.insert(0, generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    website = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message="Make sure no fields are empty.")
    else:
        load_to_file(new_data)

def load_to_file(new_data):
    try:
        with open("saves.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        with open("saves.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
        data.update(new_data)

        with open("saves.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    finally:
        web_entry.delete(0, END)
        password_entry.delete(0, END)

def search():

    try:
        with open("saves.json", "r") as data_file:
            data = json.load(data_file)
            website = web_entry.get()
            saved_email = data.get(website).get("email")
            saved_password = data.get(website).get("password")

            password_entry.delete(0, END)
            username_entry.delete(0,END)
            password_entry.insert(0, saved_password)
            username_entry.insert(0, saved_email)


    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Password file is empty.")
    
    except AttributeError:
        messagebox.showinfo(title="Oops", message="No saved password for site.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", font=(FONT_NAME, 10))
web_label.grid(row=1, column=0)
web_entry = Entry(width=32)
web_entry.grid(row=1, column=1, columnspan=1)
web_entry.focus()
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)


username_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
username_label.grid(row=2, column=0)
username_entry = Entry(width=50)
username_entry.insert(0, "mataniwani1999@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(row=3, column=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, columnspan=1)
password_button= Button(text="Generate Password",width=13, command=generate)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()