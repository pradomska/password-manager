from tkinter import *
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def save_passwd():
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

button_gen = Button(text="Generate", font=(FONT_NAME, 8, "normal"), relief="raised", width=18)
button_gen.grid(row=3, column=2)

button_add = Button(text="Add", font=(FONT_NAME, 8, "normal"), relief="raised", width=51, command=save_passwd)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
