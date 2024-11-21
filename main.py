import tkinter
from treeview_frame import TreeviewFrame

window = tkinter.Tk()
window.title("4kitsw10_COM519")

treeview_one = TreeviewFrame("4kitsw10_COM519_database", window, ["one", "two", "three"])
treeview_one.render()
treeview_one.clear()

TreeviewFrame("4kitsw10_COM519_database", window, ["four", "five", "six"]).render(window)

window.mainloop()