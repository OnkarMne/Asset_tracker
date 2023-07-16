from tkinter import *
from tkinter import messagebox
import admin_form


def open_login_form():
    def login():
        if userid_entry.get() == "Admin" and password_entry.get() == "admin123":
            admin_form.open_admin_form()
            login_window.destroy()
        else:
            messagebox.showinfo(message="Incorrect credentials")
            login_window.destroy()

    login_window = Tk()
    login_window.title("Admin Login")
    login_window.config(padx=50, pady=50)

    userid_label = Label(login_window, text="User Name:")
    userid_label.grid(row=1, column=0)
    userid_entry = Entry(login_window, width=30)
    userid_entry.grid(row=1, column=1, padx=5)

    password_label = Label(login_window, text="Password:")
    password_label.grid(row=2, column=0)
    password_entry = Entry(login_window, show="*", width=30)
    password_entry.grid(row=2, column=1, padx=5)

    login_button = Button(login_window, text="Login", width=10, command=login)
    login_button.grid(row=4, column=1, padx=10)
