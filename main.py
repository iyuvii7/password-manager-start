from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    letters_list = [choice(letters) for _ in range(randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    # # for char in range(nr_numbers):
    # #   password_list += random.choice(numbers)
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_data = website_entry.get()
    email_username_data = email_entry.get()
    password_data = password_entry.get()
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail: {email_username_data} \nPassword: {password_data}")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_data} | {email_username_data} | {password_data}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
# ---------------------------- CLEAR PASSWORD ------------------------------- #
def clear():
    password_entry.delete(0, "end")
    website_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# 3 labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

# 3 entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "suwetayuvraj9411417@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# 3 button
generate_password = Button(text="Generate password", command=generate_password)
generate_password.grid(row=3, column=2, sticky="EW")
add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2, sticky="EW")
clear_button = Button(text="Clear", command=clear)
clear_button.grid(row=4, column=0)

window.mainloop()