from tkinter import *
from tkinter import ttk

class ActionsFrame:
    def __init__(self, window):
        self.__frame = Frame(window)
        self.__treeview = None

    def render(self):
        self.__treeview = self.__render_headings()
        self.__treeview.grid(row=0, column=0)
        self.__frame.pack(fill="both", expand=True)

    def __render_headings(self):
        columns = [
            "Action",
            "Description",
        ]

        treeview = ttk.Treeview(
            self.__frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            treeview.heading(i, text=i)

        return self.__render_body(treeview)

    def __render_body(self, treeview):
        treeview.insert("", "end", values=("Manage Team Members", "temp"))
        treeview.insert("", "end", values=("Manage Menu", "temp"))
        return treeview

    def get_manage_team(self):
        item = self.__treeview.selection()[0]
        return self.__treeview.item(item, "values")[0] == "Manage Team Members"

    def get_manage_menu(self):
        item = self.__treeview.selection()[0]
        return self.__treeview.item(item, "values")[0] == "Manage Menu"

    def get_frame(self):
        return self.__frame

    def get_treeview(self):
        return self.__treeview

    def clear(self):
        for widgets in self.__frame.winfo_children():
            widgets.destroy()