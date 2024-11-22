import sqlite3
from tkinter import *
from tkinter import messagebox
from functools import partial
from login_manager import LoginManager

class LoginFrame:
    def __init__(self, database, window):
        self.__frame = Frame(window)
        self.__database = database
        self.__cursor = sqlite3.connect(database).cursor()
        self.__username = StringVar()
        self.__password = StringVar()

    def render(self):
        self.__render_username()
        self.__render_password()
        self.__render_login()
        self.__frame.pack(fill="both", expand=True)

    def __render_username(self):
        Label(self.__frame, text="Username").grid(row=0, column=0)
        Entry(self.__frame, textvariable=self.__username).grid(row=0, column=1)

    def __render_password(self):
        Label(self.__frame, text="Password").grid(row=1, column=0)
        Entry(self.__frame, textvariable=self.__password, show='*').grid(row=1, column=1)

    def __render_login(self):
        command_login = partial(self.__login, self.__username, self.__password)
        Button(self.__frame, text="Login", command=command_login).grid(row=3, column=0)

    def __login(self, username, password):
        if LoginManager(self.__database).breach(username.get(), password.get()):
            print("Login successful")

        messagebox.showwarning(
            "Login Failed",
            "The username or password you supplied are incorrect."
        )