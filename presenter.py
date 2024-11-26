import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from login_manager import LoginManager
from team_manager import TeamManager
from menu_manager import MenuManager
from nutrition_manager import NutritionManager

class Presenter:
    def __init__(self, database):
        self.__window = tkinter.Tk()
        self.__frame = tkinter.Frame(self.__window)
        self.__treeview = None
        self.__database = database
        self.__login_manager = LoginManager(database)
        self.__team_manager = TeamManager(database)
        self.__menu_manager = MenuManager(database)
        self.__nutrition_manager = NutritionManager(database)

    def render(self):
        self.__window.title("4kitsw10_COM519")
        self.__render_login()
        self.__window.mainloop()

    def __render_login(self):
        username = StringVar()
        password = StringVar()

        self.__window.geometry('400x250')
        self.__clear_window()
        self.__render_login_username(username)
        self.__render_login_password(password)
        self.__render_login_submit(username, password)
        self.__frame.grid(row=0, column=0)

    def __clear_window(self):
        for i in self.__frame.grid_slaves():
            i.destroy()

    def __render_login_username(self, username):
        Label(self.__frame, text="Username").grid(row=0, column=0)
        Entry(self.__frame, textvariable=username).grid(row=0, column=1)

    def __render_login_password(self, password):
        Label(self.__frame, text="Password").grid(row=1, column=0)
        Entry(self.__frame, textvariable=password, show='*').grid(row=1, column=1)

    def __render_login_submit(self, username, password):
        command_login = partial(self.__login_procedure, username, password)
        Button(self.__frame, text="Login", command=command_login).grid(row=3, column=0)

    def __login_procedure(self, username, password):
        if self.__login_manager.login(username.get(), password.get()):
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
        self.__apply_frame()

    def __apply_frame(self):
        self.__frame.grid(row=0, column=0)
        self.__window.update()

        resolution = (
            f"{self.__frame.winfo_width()}"
            f"x"
            f"{self.__frame.winfo_height()}"
        )

        self.__window.geometry(resolution)

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
            self.__frame,
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

    def __render_actions_logout(self):
        command_logout = partial(self.__render_login)
        Button(self.__frame, text="Logout", command=command_logout).grid(row=1, column=0)

    def __actions_procedure(self, event):
        item = self.__treeview.selection()[0]
        action = self.__treeview.item(item, "values")[0]

        if action == "Manage Team Members":
            self.__render_team()

        if action == "Manage Menu":
            self.__render_menu()

    def __render_team(self):
        self.__clear_window()
        self.__render_team_treeview()
        self.__render_team_back()
        self.__apply_frame()

    def __render_team_treeview(self):
        self.__render_team_headings()
        self.__render_team_body()
        self.__treeview.grid(row=0, column=0)

    def __render_team_headings(self):
        columns = [
            "Forename",
            "Surname",
            "Age",
            "Tenure",
            "Role"
        ]

        self.__treeview = ttk.Treeview(
            self.__frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_team_body(self):
        for i in self.__team_manager.get_team():
            self.__treeview.insert("", "end", values=(
                i[0],
                i[1],
                f"{i[2]} years",
                f"{i[3]} years",
                i[4]
            ))

    def __render_team_back(self):
        command_logout = partial(self.__render_actions)
        Button(self.__frame, text="Back", command=command_logout).grid(row=1, column=0)

    def __render_menu(self):
        self.__clear_window()
        self.__render_menu_treeview()
        self.__render_menu_back()
        self.__apply_frame()

    def __render_menu_treeview(self):
        self.__render_menu_headings()
        self.__render_menu_body()
        self.__treeview.bind("<Double-1>", self.__menu_nutrition_procedure)
        self.__treeview.grid(row=0, column=0)

    def __render_menu_headings(self):
        columns = [
            "Name",
            "RSP",
            "Calories"
        ]

        self.__treeview = ttk.Treeview(
            self.__frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_menu_body(self):
        for i in self.__menu_manager.get_menu():
            self.__treeview.insert("", "end", values=(
                i[1],
                f"£{i[2]}",
                f"{i[3]} cals"
            ))

    def __menu_nutrition_procedure(self, event):
        item = self.__treeview.selection()[0]
        nutrition = self.__treeview.item(item, "values")[0]

        self.__render_nutrition(nutrition)

    def __render_menu_back(self):
        command_logout = partial(self.__render_actions)
        Button(self.__frame, text="Back", command=command_logout).grid(row=1, column=0)

    def __render_nutrition(self, nutrition):
        self.__clear_window()
        self.__render_nutrition_treeview(nutrition)
        self.__apply_frame()

    def __render_nutrition_treeview(self, nutrition):
        self.__render_nutrition_headings()
        self.__render_nutrition_body(nutrition)
        self.__treeview.grid(row=0, column=0)

    def __render_nutrition_headings(self):
        columns = [
            "Ingredient",
            "Quantity",
            "Total Weight",
            "Total Calories"
        ]

        self.__treeview = ttk.Treeview(
            self.__frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_nutrition_body(self, nutrition):
        for i in self.__nutrition_manager.get_nutrition(nutrition):
            self.__treeview.insert("", "end", values=(
                i[1],
                f"x{i[2]}",
                f"{i[3]}g",
                f"{i[4]} cals"
            ))