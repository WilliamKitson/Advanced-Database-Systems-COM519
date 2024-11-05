import tkinter
import sqlite3
from tkinter import ttk

class CustomerMenuPage:
    def __init__(self):
        self.__treeview = ttk.Treeview(columns=("size", "lastmod"))

        connection_obj = sqlite3.connect("4kitsw10_COM519_database")
        self.__cursor = connection_obj.cursor()

    def render(self):
        self.__treeview.heading("#0", text="Name")
        self.__treeview.heading("size", text="RSP")
        self.__treeview.heading("lastmod", text="Calories")

        self.__cursor.execute(f"SELECT * FROM Customer_Facing_Menu")

        for row in self.__cursor.fetchall():
            self.__treeview.insert(
                "",
                tkinter.END,
                text=row[1],
                values=(row[2], row[3])
            )

        self.__treeview.pack()