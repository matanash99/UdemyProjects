"""
Miles to Km Converter
"""

from tkinter import *


def button_clicked():
    miles = float(user_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km:.2f}")
    print("I got clicked")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width= 100, height= 100)
window.config(pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column= 3, row= 1)


button = Button(text="Calculate", command= button_clicked)
button.grid(column= 1, row= 3)

user_input = Entry(width= 10)
user_input.grid(column= 2, row= 1)

is_equal_to = Label(text= f"is equal to")
is_equal_to.grid(column= 0, row= 2)

km_label = Label(text= "Km")
km_label.grid(column= 3, row= 2)

result = 0
result_label = Label(text= f"{result}")
result_label.grid(column= 2, row= 2)


window.mainloop()