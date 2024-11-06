import sqlite3
from tkinter import ttk

class Page:
    def __init__(self, database, window, columns):
        self._database = database
        self._cursor = sqlite3.connect(database).cursor()
        self._window = window
        self._treeview = self.__initialise_treeview(columns)

    def __initialise_treeview(self, columns):
        tree = ttk.Treeview(self._window, columns=columns, show="headings")

        for i in columns:
            tree.heading(i, text=i)

        return tree