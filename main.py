import tkinter
from treeview_frame import TreeviewFrame

window = tkinter.Tk()
window.title("4kitsw10_COM519")

TreeviewFrame("4kitsw10_COM519_database", ["one", "two", "three"]).render(window)
TreeviewFrame("4kitsw10_COM519_database", ["four", "five", "six"]).render(window)

window.mainloop()