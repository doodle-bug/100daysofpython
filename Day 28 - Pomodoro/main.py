from tkinter import *
import math
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
    #  after_cancel closes the after timer
    window.after_cancel(timer)
    title.config(text="Timer", fg="blue")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Relax", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # floor() returns the largest integer <= x
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # itemconfig - used to configure the parameters of a canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # after() - excute a command after a time delay
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check_marks.config(text=mark)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# size of tomato image is taken
# highlightthickness is the border outline of the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness = 0)

# PhotoImage is used to display images in labels, buttons, canvases and text widgets
tomato_img = PhotoImage(file = r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\Pomodoro\tomato.png")

# for placing image at the centre of the canvas,half of the dimension of image is taken
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill = "blue", font=[FONT_NAME, 30, "bold"])
canvas.grid(column=2, row=2)

title = Label(text="Timer", font=("Times New Roman", 35))
title.config(bg = YELLOW, fg = GREEN)
title.grid(column=2,row=1)

start = Button(text="Start",bg=PINK, command=start_timer)
start.grid(column=1,row=3)

reset = Button(text="Reset", bg=PINK, command=reset_timer)
reset.grid(column=3,row=3)

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.config(pady=20)
check_marks.grid(column=2, row=3)

window.mainloop()