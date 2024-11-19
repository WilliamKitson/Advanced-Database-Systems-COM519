import tkinter
from tkinter import *
import sqlite3
from functools import partial

class LoginPage:
    def __init__(self, database):
        self.__database = database
        self.__cursor = sqlite3.connect(database).cursor()
        self.__window = tkinter.Tk()
        self.__window.title("login")
        self.__window.geometry('400x250')
        self.__username = StringVar()
        self.__password = StringVar()

    def render(self):
        self.__render_username()
        self.__render_password()

        command_login = partial(self.__login, self.__username, self.__password)
        Button(self.__window, text="Login", command=command_login).grid(row=3, column=0)


        self.__window.mainloop()

    def __render_username(self):
        Label(self.__window, text="Username").grid(row=0, column=0)

        Entry(self.__window, textvariable=self.__username).grid(row=0, column=1)

    def __render_password(self):
        Label(self.__window, text="Password").grid(row=1, column=0)

        Entry(self.__window, textvariable=self.__password, show='*').grid(row=1, column=1)

    def __login(self, username, password):
        print("test")