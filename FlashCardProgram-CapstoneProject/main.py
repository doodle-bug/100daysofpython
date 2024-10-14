from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# creaing empty dictionaries for storing data
current_card = {}
to_learn = {}

# this will be used when words_to_learn.csv file is not there
try:
    data = pandas.read_csv(r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\FlashCardProgram-CapstoneProject\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # (orient="records") changes the orientation of data in the dictionary
    to_learn = data.to_dict(orient="records")


"""---------------------Next Card-------------------"""
def next_card():
    global current_card, flip_timer
    # .after_cancel() is used to cancel the callback of window.after()
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    word = current_card["French"]
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = word, fill = "black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    e_word = current_card["English"]
    canvas.itemconfig(card_word, text = e_word, fill = "white")
    canvas.itemconfig(card_background, image=card_back)
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    # index=False is used to remove the index from the dataframe
    data.to_csv("words_to_learn.csv", index=False)

    next_card()

"""----------------------UI Setup-------------------"""
window = Tk()
window.title("FLashy")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

# calls the flip_card function after 3000ms
flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file = r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\FlashCardProgram-CapstoneProject\images\card_front.png")
card_back = PhotoImage(file=r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\FlashCardProgram-CapstoneProject\images\card_back.png")
card_background = canvas.create_image(400, 263, image = card_front)
card_title = canvas.create_text(400, 150, text="", font = ("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font = ("Arial", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file=r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\FlashCardProgram-CapstoneProject\images\wrong.png")
unknown_button = Button(image = cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0,row=1)

tick_image = PhotoImage(file=r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\FlashCardProgram-CapstoneProject\images\right.png")
known_button = Button(image=tick_image, highlightthickness=0, command=is_known)
known_button.grid(column=1,row=1)

next_card()

window.mainloop()

