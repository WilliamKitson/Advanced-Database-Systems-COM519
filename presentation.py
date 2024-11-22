import tkinter
from login_frame import LoginFrame
from menu_items_frame import MenuItemsFrame
from team_members_frame import TeamMembersFrame

class Presentation:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")

    def render(self):
        LoginFrame("4kitsw10_COM519_database", self.__window).render()
        MenuItemsFrame("4kitsw10_COM519_database", self.__window).render()
        TeamMembersFrame("4kitsw10_COM519_database", self.__window).render()
        self.__window.mainloop()