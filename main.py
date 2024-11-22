import tkinter

from login_frame import LoginFrame
from menu_items_frame import MenuItemsFrame
from team_members_frame import TeamMembersFrame

window = tkinter.Tk()
window.title("4kitsw10_COM519")

LoginFrame("4kitsw10_COM519_database", window).render()
TeamMembersFrame("4kitsw10_COM519_database", window).render()
MenuItemsFrame("4kitsw10_COM519_database", window).render()

window.mainloop()