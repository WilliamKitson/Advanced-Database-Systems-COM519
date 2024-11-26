import tkinter
from tkinter import *
from tkinter import ttk
from functools import partial

class Presenter:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title("4kitsw10_COM519")
        self.__window.geometry('400x250')

    def render(self):
        self.__render_login()
        self.__render_actions()
        self.__window.mainloop()

    def __render_login(self):
        username = StringVar()
        password = StringVar()

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
        command_login = partial(self.__TEMP_login_procedure, username, password)
        Button(self.__window, text="Login", command=command_login).grid(row=3, column=0)

    def __TEMP_login_procedure(self, username, password):
        print(f"{username.get()}:{password.get()}")

    def __render_actions(self):
        self.__clear_window()

        treeview = self.__render_actions_headings()
        treeview.grid(row=0, column=0)

        self.__render_actions_logout()

    def __clear_window(self):
        for i in self.__window.grid_slaves():
            i.destroy()

    def __render_actions_headings(self):
        columns = [
            "Action",
            "Description",
        ]

        treeview = ttk.Treeview(
            self.__window,
            columns=columns,
            show="headings"
        )

        for i in columns:
            treeview.heading(i, text=i)

        return self.__render_actions_body(treeview)

    def __render_actions_body(self, treeview):
        treeview.insert("", "end", values=("Manage Team Members", "temp"))
        treeview.insert("", "end", values=("Manage Menu", "temp"))
        return treeview

    def __render_actions_logout(self):
        command_logout = partial(self.__logout_process)
        Button(self.__window, text="Logout", command=command_logout).grid(row=1, column=0)

    def __logout_process(self):
        print("logout process")