import sqlite3
from tkinter import *
from tkinter import ttk
from functools import partial

class DishNutritionFrame:
    def __init__(self, database, window, dish):
        self.__frame = Frame(window)
        self._cursor = sqlite3.connect(database).cursor()
        self.__dish = dish

    def render(self):
        self.__render_headings()
        self.__render_back()
        self.__frame.pack(fill="both", expand=True)

    def __render_headings(self):
        columns = [
            "Forename",
            "Surname",
            "Age",
            "Tenure",
            "Role"
        ]

        treeview = ttk.Treeview(
            self.__frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            treeview.heading(i, text=i)

        self.__render_body(treeview)

    def __render_body(self, treeview):
        self._cursor.execute(
            "SELECT * "
            "FROM Menu_Item_Neutrition "
            "WHERE Menu_Item_Neutrition.Menu_Item=?",
            (self.__dish,)
        )

        for row in self._cursor.fetchall():
            treeview.insert("", "end", values=(
                row[1],
                row[2],
                f"{row[3]}g",
                f"{row[4]} cals"
            ))

        treeview.grid(row=0, column=0)

    def __render_back(self):
        command_login = partial(self.clear)
        Button(self.__frame, text="Back", command=command_login).grid(row=2, column=0)

    def clear(self):
        for widgets in self.__frame.winfo_children():
            widgets.destroy()