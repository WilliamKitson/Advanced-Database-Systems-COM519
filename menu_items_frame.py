import sqlite3
from tkinter import *
from tkinter import ttk

class MenuItemsFrame:
    def __init__(self, database, window):
        self.__frame = Frame(window)
        self._cursor = sqlite3.connect(database).cursor()

    def render(self):
        treeview = self.__render_headings()
        treeview.grid(row=0, column=0)
        self.__frame.pack(fill="both", expand=True)


    def __render_headings(self):
        columns = [
            "Name",
            "RSP",
            "Calories"
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
        self._cursor.execute(
            "SELECT * "
            "FROM Customer_Facing_Menu"
        )

        for row in self._cursor.fetchall():
            treeview.insert("", "end", values=(
                row[1],
                f"£{row[2]}",
                f"{row[3]} cals"
            ))

        return treeview

    def clear(self):
        for widgets in self.__frame.winfo_children():
            widgets.destroy()