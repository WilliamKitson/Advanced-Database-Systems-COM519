import sqlite3
from tkinter import *
from tkinter import ttk

class TreeviewFrame:
    def __init__(self, database, window):
        self.__frame = Frame(window)

    def render(self):
        treeview = self.__render_headings()
        treeview.grid(row=0, column=0)
        self.__frame.pack(fill="both", expand=True)

    def __render_headings(self):
        columns = [
            "Forename",
            "Surname",
            "Age",
            "Tenure",
            "Role"
        ]

        treeview = ttk.Treeview(self.__frame, columns=columns, show="headings")

        for i in columns:
            treeview.heading(i, text=i)

        return treeview

    def clear(self):
        for widgets in self.__frame.winfo_children():
            widgets.destroy()