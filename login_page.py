import sqlite3
import tkinter
from tkinter import ttk

class LoginPage:
    def __init__(self, database):
        self._database = database
        self._cursor = sqlite3.connect(database).cursor()
        self._window = tkinter.Tk()
        self._window.title("login")

    def render(self):
        self._window.mainloop()