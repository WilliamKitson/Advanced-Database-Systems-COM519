import tkinter
from tkinter import *
from functools import partial
from login_frame import LoginFrame
from actions_frame import ActionsFrame
from menu_items_frame import MenuItemsFrame

class Presentation:
    def __init__(self, database):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')
        self.__login_frame = LoginFrame(database, self.__window)
        self.__actions_frame = ActionsFrame(self.__window)
        self.__menu_items = MenuItemsFrame(database, self.__window)

    def render(self):
        self.__assemble_login()
        self.__window.mainloop()

    def __assemble_login(self):
        self.__login_frame.render()
        self.__render_login_button()

    def __render_login_button(self):
        command_login = partial(self.__login_procedure)
        Button(self.__login_frame.get_frame(), text="Login", command=command_login).grid(row=3, column=0)

    def __login_procedure(self):
        self.__login_frame.login()

        if self.__login_frame.get_logged_in() is not None:
            self.__login_frame.clear()
            self.__actions_frame.render()
            self.__render_logout_button()

    def __render_logout_button(self):
        command_login = partial(self.__logout_process)
        Button(self.__menu_items.get_frame(), text="Logout", command=command_login).grid(row=1, column=0)

    def __logout_process(self):
        self.__menu_items.clear()
        self.__assemble_login()