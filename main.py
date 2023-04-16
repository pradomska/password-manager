from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Courier"


def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = ''.join(password_list)

    entry_passwd.insert(0, password)
    pyperclip.copy(password)


def save_passwd():
    if len(entry_web.get()) == 0 or len(entry_login.get()) == 0 or len(entry_passwd.get()) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=entry_web.get(),
                                       message=f"These are the details entered: \nEmail: {entry_login.get()}"
                                               f"\nPassword: {entry_passwd.get()} \nIs it ok to save?")
        if is_ok:
            with open("passwd.txt", mode="a") as data:
                data.write(f"{entry_web.get()} | {entry_login.get()} | {entry_passwd.get()}\n")
                entry_web.delete(0, END)
                entry_passwd.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label_web = Label(text="Website:", font=FONT_NAME)
label_web.grid(row=1, column=0)

label_login = Label(text="Email/Username:", font=FONT_NAME)
label_login.grid(row=2, column=0)

label_passwd = Label(text="Password:", font=FONT_NAME)
label_passwd.grid(row=3, column=0)

entry_web = Entry(width=60)
entry_web.focus()
entry_web.grid(row=1, column=1, columnspan=2)

entry_login = Entry(width=60)
entry_login.insert(END, "example@email.com")
entry_login.grid(row=2, column=1, columnspan=2)

entry_passwd = Entry(width=37)
entry_passwd.grid(row=3, column=1)

button_gen = Button(text="Generate", font=(FONT_NAME, 8, "normal"), relief="raised", width=18, command=generate_passwd)
button_gen.grid(row=3, column=2)

button_add = Button(text="Add", font=(FONT_NAME, 8, "normal"), relief="raised", width=51, command=save_passwd)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
