import tkinter
from team_members_frame import TeamMembersFrame

window = tkinter.Tk()
window.title("4kitsw10_COM519")

treeview_one = TeamMembersFrame("4kitsw10_COM519_database", window)
treeview_one.render()
treeview_one.clear()

TeamMembersFrame("4kitsw10_COM519_database", window).render()

window.mainloop()