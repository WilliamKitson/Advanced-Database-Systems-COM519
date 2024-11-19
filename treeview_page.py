import sqlite3
import tkinter
from tkinter import ttk

class TreeviewPage:
    def __init__(self, database, title, columns):
        self._database = database
        self._cursor = sqlite3.connect(database).cursor()
        self._window = tkinter.Tk()
        self._window.title(title)
        self._treeview = self.__initialise_treeview(columns)

    def __initialise_treeview(self, columns):
        tree = ttk.Treeview(self._window, columns=columns, show="headings")

        for i in columns:
            tree.heading(i, text=i)

        return tree