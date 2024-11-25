import sqlite3
from tkinter import *
from tkinter import ttk
from functools import partial

class TeamMembersFrame:
    def __init__(self, database, window):
        self.__frame = Frame(window)
        self._cursor = sqlite3.connect(database).cursor()

    def render(self):
        self.__render_headings()
        self.__render_add()
        self.__frame.grid(column=0, row=0)

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
            "FROM View_Team_Members"
        )

        for row in self._cursor.fetchall():
            treeview.insert("", "end", values=(
                row[0],
                row[1],
                f"{row[2]} years",
                f"{row[3]} years",
                row[4]
            ))

        treeview.grid(row=0, column=0)

    def __render_add(self):
        command_login = partial(self.__add_staff)
        Button(self.__frame, text="Add Staff", command=command_login).grid(row=1, column=0)

    def __add_staff(self):
        print("Adding staff members")