import tkinter
from login_frame import LoginFrame
from menu_items_frame import MenuItemsFrame
from team_members_frame import TeamMembersFrame

class Presentation:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')

    def render(self):
        LoginFrame("4kitsw10_COM519_database", self.__window).render()
        self.__window.mainloop()