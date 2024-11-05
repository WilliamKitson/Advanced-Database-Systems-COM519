import tkinter
import sqlite3
from tkinter import ttk
from tkinter import *

class CustomerMenuPage:
    def __init__(self, window):
        self.__window = window
        self.__treeview = self.__initialise_treeview()
        self.__cursor = self.__initialise_cursor()

    def __initialise_treeview(self):
        headers = (
            'Name',
            'RSP',
            'Calories',
            "Order"
        )

        tree = ttk.Treeview(self.__window, columns=headers, show='headings')

        for i in headers:
            tree.heading(i, text=i)

        return tree

    @staticmethod
    def __initialise_cursor():
        connection_obj = sqlite3.connect("4kitsw10_COM519_database")
        return connection_obj.cursor()

    def render(self):
        self.__render_buttons()
        self.__render_table()

    def __render_buttons(self):
        self.__cursor.execute(f"SELECT * FROM Categories")

        for row in self.__cursor.fetchall():
            turn_on = Button(self.__window, text=f"{row}s")
            turn_on.pack()

    def __render_table(self):
        self.__cursor.execute(f"SELECT * FROM Customer_Facing_Menu")

        for row in self.__cursor.fetchall():
            self.__treeview.insert("", "end", values=(
                row[1],
                f"£{row[2]}",
                f"{row[3]} cals",
                "temp"
            ))

        self.__treeview.pack()