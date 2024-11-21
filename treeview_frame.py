import sqlite3
from tkinter import *
from tkinter import ttk

class TreeviewFrame:
    def __init__(self, database, window, columns):
        self._database = database
        self._cursor = sqlite3.connect(database).cursor()
        self._columns = columns
        self.__frame = Frame(window)

    def render(self):
        treeview = ttk.Treeview(self.__frame, columns=self._columns, show="headings")

        for i in self._columns:
            treeview.heading(i, text=i)

        treeview.grid(row=0, column=0)

        self.__frame.pack(fill="both", expand=True)

    def clear(self):
        for widgets in self.__frame.winfo_children():
            widgets.destroy()