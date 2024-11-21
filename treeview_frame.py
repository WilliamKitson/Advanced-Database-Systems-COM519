import sqlite3
from tkinter import *
from tkinter import ttk

class TreeviewFrame:
    def __init__(self, database, columns):
        self._database = database
        self._cursor = sqlite3.connect(database).cursor()
        self._columns = columns

    def render(self, window):
        frame = Frame(window)

        treeview = ttk.Treeview(frame, columns=self._columns, show="headings")

        for i in self._columns:
            treeview.heading(i, text=i)

        treeview.grid(row=0, column=0)

        frame.pack(fill="both", expand=True)