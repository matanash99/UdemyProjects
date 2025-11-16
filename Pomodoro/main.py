import math
from tkinter import *
from turtledemo.chaos import coosys

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    check_label.config(text="")
    window.after_cancel(timer)
    title_label.config(text="Timer", fg= GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text= "Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=GREEN)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=RED)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start()
        work_sessions = math.floor(reps/2)
        checks_str = ""
        for _ in range(work_sessions):
            checks_str += "✓"
        check_label.config(text= checks_str)
        check_label.grid(column=2, row=4)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50,bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50), bg= YELLOW, fg= GREEN)
title_label.grid(column= 2, row= 1)


check_label = Label(text="✓", font=(FONT_NAME, 20), bg= YELLOW, fg= GREEN)

start_button = Button(text= "Start", command=start)
start_button.grid(column= 1, row= 3)

reset_button = Button(text= "Reset", command=reset_timer)
reset_button.grid(column= 3, row= 3)

canvas = Canvas(width= 200, height= 224,bg=YELLOW,highlightthickness=0)
image_file = PhotoImage(file= "tomato.png")
canvas.create_image(100, 111, image=image_file)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column= 2, row= 2)























window.mainloop()