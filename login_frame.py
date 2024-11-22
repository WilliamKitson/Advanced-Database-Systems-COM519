import sqlite3
from tkinter import *
from tkinter import messagebox

class LoginFrame:
    def __init__(self, database, window):
        self.__frame = Frame(window)
        self.__database = database
        self.__cursor = sqlite3.connect(database).cursor()
        self.__username = StringVar()
        self.__password = StringVar()
        self.__logged_in = None

    def render(self):
        self.__render_username()
        self.__render_password()
        self.__frame.pack(fill="both", expand=True)

    def __render_username(self):
        Label(self.__frame, text="Username").grid(row=0, column=0)
        Entry(self.__frame, textvariable=self.__username).grid(row=0, column=1)

    def __render_password(self):
        Label(self.__frame, text="Password").grid(row=1, column=0)
        Entry(self.__frame, textvariable=self.__password, show='*').grid(row=1, column=1)

    def login(self):
        query = (
            "SELECT * "
            "FROM Staff "
            "WHERE Username = ? "
            "AND Password = ? "
        )

        self.__cursor.execute(query, (self.__username.get(), self.__password.get()))

        for row in self.__cursor.fetchall():
            self.__logged_in = row[0]
            return

        messagebox.showwarning(
            "Login Failed",
            "The username or password you supplied are incorrect."
        )

    def get_frame(self):
        return self.__frame

    def get_logged_in(self):
        return self.__logged_in

    def clear(self):
        for widgets in self.__frame.winfo_children():
            widgets.destroy()