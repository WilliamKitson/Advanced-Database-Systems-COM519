import tkinter
from tkinter import *
from functools import partial
from login_frame import LoginFrame
from menu_items_frame import MenuItemsFrame
from team_members_frame import TeamMembersFrame

class Presentation:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')

    def render(self):
        login_frame = LoginFrame("4kitsw10_COM519_database", self.__window)
        login_frame.render()

        command_login = partial(login_frame.login)
        Button(login_frame.get_frame(), text="Login", command=command_login).grid(row=3, column=0)

        self.__window.mainloop()