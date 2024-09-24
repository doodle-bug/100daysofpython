from tkinter import *

def button_clicked():
    # print("I got clicked")
    new_text = float(input.get()) * 1.609
    my_label2.config(text = new_text)

window = Tk()
window.title("Miles to Km Calculator")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

my_label4 = Label(text="", font=("Arial", 12))
my_label4.grid(column=1,row=1)
my_label4.config(padx=10, pady=10)

input = Entry(width=15)
input.grid(column=4,row=2)


my_label = Label(text="Miles", font=("Arial", 12))
my_label.grid(column=5,row=2)
my_label.config(padx=10, pady=10)

my_label1 = Label(text="is equal to", font=("Arial", 12))
my_label1.grid(column=3,row=3)
my_label1.config(padx=10, pady=10)

my_label2 = Label(text="0", font=("Arial", 12))
my_label2.grid(column=4,row=3)
my_label2.config(padx=10, pady=10)

my_label3 = Label(text="Kms", font=("Arial", 12))
my_label3.grid(column=5,row=3)
my_label3.config(padx=10, pady=10)

button = Button(text="Calculate", command = button_clicked)
button.grid(column=4,row=4)








window.mainloop()