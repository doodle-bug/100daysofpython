from tkinter import *
# messagebox is not a class but a module, so we have to import it separately
from tkinter import messagebox
import random
import pyperclip
import json
        
"""-----------------------Password Generator------------------------"""
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(symbols) for _ in range(nr_symbols)]
    password_symbols = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    # join is used to join the element in a list/tuple and "" means the elements are sparated by whatever is inside ""
    password = "".join(password_list)
    entry3.insert(0, password)
    # used to copy the string in the clipboard
    pyperclip.copy(password)


"""-------------------------Saved Password--------------------------"""
def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure every field is filled properly.")
    else:
        # using files in json to put it in proper format
        """
        If you try to read an empty json file using load or the file is not present, it will throw an error
        """
        try:
            with open("data.json", "r") as data_file:
                # dump is used to add items in the file
                # indent is used to indent the data for better readability
                # json.dump(new_data, data_file, indent=4)
                # load is used to read the data
                """reading old data"""
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        # else executes only when try statement executes
        else:
            # update is used to append data into the file
            """updating old data with new data in the same dictionary"""
            data.update(new_data)
            with open("data.json", "w") as data_file:
                """saving updated data"""
                json.dump(data, data_file, indent=4)

        # finally executes irrespective of the above exception handling conditions
        finally:
            # clears the input from start to end
            entry1.delete(0, END)
            entry3.delete(0, END)

"""-------------------------Saved Password--------------------------"""
def find_password():
    website = entry1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops! Error", message="Data File Not Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Oops! Error", message="Website Not Found.")

            
"""----------------------------UI Setup-----------------------------"""
# creating canvas in window

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

lock = PhotoImage(file = r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\Day 29 - Password Generator\logo.png")
canvas.create_image(100, 100, image = lock)
canvas.grid(column=2, row=1)

label1 = Label(text="Website:", font=("Arial", 10))
label1.grid(column=1,row=2)

label2 = Label(text="Email/Username:", font=("Arial", 10))
label2.grid(column=1,row=3)

label3 = Label(text="Password:", font=("Arial", 10))
label3.grid(column=1,row=4)

entry1 = Entry(width=34)
entry1.grid(column=2,row=2)
# moves the cursur to ths entry
entry1.focus()

entry2 = Entry(width=52)
entry2.grid(column=2,row=3, columnspan=2)
# pre filled the entry block with this text ,0 represent to filled it at the start
entry2.insert(0, "amitanand@gmail.com")

entry3 = Entry(width=34)
entry3.grid(column=2,row=4)

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(column=3,row=4)

button2 = Button(text="Add", width=44, command=save)
button2.grid(column=2,row=5, columnspan=2)

button3 = Button(text="Search",width = 14, command=find_password)
button3.grid(column=3,row=2)












window.mainloop()