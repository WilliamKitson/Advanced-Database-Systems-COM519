import tkinter
from tkinter import *
import sqlite3

class LoginPage:
    def __init__(self, database):
        self.__database = database
        self.__cursor = sqlite3.connect(database).cursor()
        self.__window = tkinter.Tk()
        self.__window.title("login")
        self.__window.geometry('400x250')

    def render(self):
        self.__render_username()

        Label(self.__window, text="Password").grid(row=1, column=0)
        password = StringVar()
        Entry(self.__window, textvariable=password, show='*').grid(row=1, column=1)

        Button(self.__window, text="Login", command="self.__login").grid(row=3, column=0)

        self.__window.mainloop()

    def __render_username(self):
        Label(self.__window, text="Username").grid(row=0, column=0)
        username = StringVar()
        Entry(self.__window, textvariable=username).grid(row=0, column=1)

    def __login(self, username, password):
        print("test")