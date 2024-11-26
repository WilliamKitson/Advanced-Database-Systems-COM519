import tkinter
from tkinter import *
from functools import partial

class Presenter:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')

    def render(self):
        self.__render_login()
        self.__window.mainloop()

    def __render_login(self):
        username = StringVar()
        password = StringVar()

        self.__render_login_username(username)
        self.__render_login_password(password)
        self.__render_login_submit(username, password)

    def __render_login_username(self, username):
        Label(self.__window, text="Username").grid(row=0, column=0)
        Entry(self.__window, textvariable=username).grid(row=0, column=1)

    def __render_login_password(self, password):
        Label(self.__window, text="Password").grid(row=1, column=0)
        Entry(self.__window, textvariable=password, show='*').grid(row=1, column=1)

    def __render_login_submit(self, username, password):
        command_login = partial(self.__TEMP_login_procedure, username, password)
        Button(self.__window, text="Login", command=command_login).grid(row=3, column=0)

    def __TEMP_login_procedure(self, username, password):
        print(f"{username.get()}:{password.get()}")