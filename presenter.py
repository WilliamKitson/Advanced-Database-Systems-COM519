import tkinter
from tkinter import *
from functools import partial

class Presenter:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')

    def render(self):
        username = StringVar()
        password = StringVar()

        Label(self.__window, text="Username").grid(row=0, column=0)
        Entry(self.__window, textvariable=username).grid(row=0, column=1)

        Label(self.__window, text="Password").grid(row=1, column=0)
        Entry(self.__window, textvariable=password, show='*').grid(row=1, column=1)

        command_login = partial(self.__TEMP_login_procedure)
        Button(self.__window, text="Login", command=command_login).grid(row=3, column=0)

        self.__window.mainloop()

    def __TEMP_login_procedure(self):
        print("temp login procedure")