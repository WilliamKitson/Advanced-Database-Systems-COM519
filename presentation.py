import tkinter
from tkinter import *
from functools import partial
from login_frame import LoginFrame
from menu_items_frame import MenuItemsFrame

class Presentation:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')
        self.__login_frame = LoginFrame("4kitsw10_COM519_database", self.__window)

    def render(self):
        self.__login_frame.render()

        command_login = partial(self.login_procedure)
        Button(self.__login_frame.get_frame(), text="Login", command=command_login).grid(row=3, column=0)

        self.__window.mainloop()

    def login_procedure(self):
        self.__login_frame.login()

        if self.__login_frame.get_logged_in() is not None:
            self.__login_frame.clear()
            MenuItemsFrame("4kitsw10_COM519_database", self.__window).render()