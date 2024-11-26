import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from login_manager import LoginManager

class Presenter:
    def __init__(self, database):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')
        self.__treeview = None
        self.__database = database

    def render(self):
        self.__render_login()
        self.__window.mainloop()

    def __render_login(self):
        username = StringVar()
        password = StringVar()

        self.__clear_window()
        self.__render_login_username(username)
        self.__render_login_password(password)
        self.__render_login_submit(username, password)

    def __render_login_username(self, username):
        Label(self.__window, text="Username").grid(row=0, column=0)
        Entry(self.__window, textvariable=username).grid(row=0, column=1)

    def __render_login_password(self, password):
        Label(self.__window, text="Password").grid(row=1, column=0)
        Entry(self.__window, textvariable=password, show='*').grid(row=1, column=1)

    def __render_login_submit(self, username, password):
        command_login = partial(self.__login_procedure, username, password)
        Button(self.__window, text="Login", command=command_login).grid(row=3, column=0)

    def __login_procedure(self, username, password):
        login_manager = LoginManager(self.__database)

        if login_manager.login(username.get(), password.get()):
            self.__render_actions()
            return

        messagebox.showwarning(
            "Login Failed",
            "The username or password you supplied are incorrect."
        )

    def __render_actions(self):
        self.__clear_window()
        self.__render_actions_treeview()
        self.__render_actions_logout()

    def __clear_window(self):
        for i in self.__window.grid_slaves():
            i.destroy()

    def __render_actions_treeview(self):
        self.__render_actions_headings()
        self.__render_actions_body()
        self.__treeview.bind("<Double-1>", self.__actions_procedure)
        self.__treeview.grid(row=0, column=0)

    def __render_actions_headings(self):
        columns = [
            "Action",
            "Description",
        ]

        self.__treeview = ttk.Treeview(
            self.__window,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_actions_body(self):
        columns = [
            "Manage Team Members",
            "Manage Menu"
        ]

        for i in columns:
            self.__treeview.insert("", "end", values=(i, "temp"))

    def __actions_procedure(self, event):
        item = self.__treeview.selection()[0]
        action = self.__treeview.item(item, "values")[0]

        if action == "Manage Team Members":
            print("manage team members")

        if action == "Manage Menu":
            print("manage menu")

    def __render_actions_logout(self):
        command_logout = partial(self.__render_login)
        Button(self.__window, text="Logout", command=command_logout).grid(row=1, column=0)