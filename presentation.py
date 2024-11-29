#  Copyright (c) 2024. William E. Kitson

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from functools import partial
from login_manager import LoginManager
from team_manager import TeamManager
from roles_manager import RolesManager
from menu_manager import MenuManager
from nutrition_manager import NutritionManager

class Presentation:
    def __init__(self, database):
        self.__window = tkinter.Tk()
        self.__instructions_frame = tkinter.Frame(self.__window)
        self.__body_frame = tkinter.Frame(self.__window)
        self.__actions_frame = tkinter.Frame(self.__window)
        self.__treeview = None
        self.__database = database

    def render(self):
        self.__window.title("4kitsw10_COM519")
        self.__window.resizable(False, False)
        self.__render_login()
        self.__window.mainloop()

    def __render_login(self):
        instructions = (
            "Welcome to William E. Kitson's COM519 project.\n"
            "Please login below to continue.\n"
            "The default admin login is Username: u, Password: p\n"
        )

        username = StringVar()
        password = StringVar()

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_login_username(username)
        self.__render_login_password(password)
        self.__render_login_submit(username, password)
        self.__apply_frame()

    def __clear_window(self):
        for i in self.__instructions_frame.grid_slaves():
            i.destroy()

        for i in self.__body_frame.grid_slaves():
            i.destroy()

        for i in self.__actions_frame.grid_slaves():
            i.destroy()

    def __render_instructions(self, instructions):
        Label(self.__instructions_frame, text=instructions).grid(row=0, column=0)

    def __render_login_username(self, username):
        Label(self.__body_frame, text="Username").grid(row=0, column=0)
        Entry(self.__body_frame, textvariable=username).grid(row=0, column=1)

    def __render_login_password(self, password):
        Label(self.__body_frame, text="Password").grid(row=1, column=0)
        Entry(self.__body_frame, textvariable=password, show='*').grid(row=1, column=1)

    def __render_login_submit(self, username, password):
        command_login = partial(self.__login_procedure, username, password)
        Button(self.__actions_frame, text="Login", command=command_login).grid(row=0, column=0)

    def __login_procedure(self, username, password):
        if LoginManager(self.__database).login(username.get(), password.get()):
            self.__render_actions()
            return

        messagebox.showwarning(
            "Login Failed",
            "The username or password you supplied are incorrect."
        )

    def __apply_frame(self):
        self.__instructions_frame.grid(row=0, column=0)
        self.__body_frame.grid(row=1, column=0)
        self.__actions_frame.grid(row=2, column=0)
        self.__window.update()
        self.__window.geometry(f"{self.__calculate_frame_width()}x{self.__calculate_frame_height()}")

    def __calculate_frame_width(self):
        width = self.__instructions_frame.winfo_width()

        if self.__body_frame.winfo_width() > width:
            width = self.__body_frame.winfo_width()

        if self.__actions_frame.winfo_width() > width:
            width = self.__actions_frame.winfo_width()

        return width

    def __calculate_frame_height(self):
        return (
            self.__instructions_frame.winfo_height() +
            self.__body_frame.winfo_height() +
            self.__actions_frame.winfo_height()
        )

    def __render_actions(self):
        instructions = (
            "Welcome to the Actions page.\n"
            "Here, you can drill into the system's subsystems by double-clicking the appropriate actions.\n"
        )

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_actions_treeview()
        self.__render_actions_logout()
        self.__apply_frame()

    def __render_actions_treeview(self):
        self.__render_actions_headings()
        self.__render_actions_body()
        self.__treeview.bind("<Double-1>", self.__actions_procedure)
        self.__treeview.grid(row=0, column=0)

    def __render_actions_headings(self):
        columns = [
            "Action",
        ]

        self.__treeview = ttk.Treeview(
            self.__body_frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_actions_body(self):
        columns = [
            "Manage Team Members",
            "Manage Menu",
            "Backup to XML"
        ]

        for i in columns:
            self.__treeview.insert("", "end", values=(i,))

    def __render_actions_logout(self):
        command_logout = partial(self.__render_login)
        Button(self.__actions_frame, text="Logout", command=command_logout).grid(row=0, column=0)

    def __actions_procedure(self, event):
        action = self.__get_treeview_event()

        if action == "Manage Team Members":
            self.__render_team()

        if action == "Manage Menu":
            self.__render_menu()

        if action == "Backup to XML":
            print("backup to XML")

    def __get_treeview_event(self):
        item = self.__treeview.selection()[0]
        return self.__treeview.item(item, "values")[0]

    def __render_team(self):
        instructions = (
            "Welcome to Manage Team.\n "
            "Here, you can add, delete, and modify team members.\n"
            "Double-click on a team member to modify or delete them."
        )

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_team_treeview()
        self.__render_team_add()
        self.__render_team_back()
        self.__apply_frame()

    def __render_team_treeview(self):
        self.__render_team_headings()
        self.__render_team_body()
        self.__treeview.bind("<Double-1>", self.__edit_team_procedure)
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
            self.__body_frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_team_body(self):
        for i in TeamManager(self.__database).get_team():
            self.__treeview.insert("", "end", values=(
                i[0],
                i[1],
                f"{i[2]} years",
                f"{i[3]} years",
                i[4]
            ))

    def __edit_team_procedure(self, event):
        self.__render_team_edit(0)

    def __render_team_add(self):
        command_add = partial(self.__render_add_team)
        Button(self.__actions_frame, text="Add", command=command_add).grid(row=1, column=0)

    def __render_add_team(self):
        instructions = (
            "Welcome to the Add Team Member Page.\n "
            "BLABLABLA."
        )

        forename = StringVar()
        surname = StringVar()
        date_of_birth = StringVar()

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_team_forename_input(forename)
        self.__render_team_surname_input(surname)
        self.__render_team_date_of_birth_input(date_of_birth)
        self.__render_add_team_save(forename, surname, date_of_birth)
        self.__render_team_back_input()
        self.__apply_frame()

    def __render_team_back(self):
        command_logout = partial(self.__render_actions)
        Button(self.__actions_frame, text="Back", command=command_logout).grid(row=1, column=1)

    def __render_team_edit(self, team_id):
        instructions = (
            "Welcome to the Edit Team Member Page.\n "
            "BLABLABLA."
        )

        username = StringVar()
        username.set("test username")

        password = StringVar()
        password.set("test password")

        forename = StringVar()
        forename.set("test forename")

        surname = StringVar()
        surname.set("test surname")

        date_of_birth = StringVar()
        date_of_birth.set("1999-01-01")

        role = StringVar()
        role.set("test role")

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_team_username_input(username)
        self.__render_team_password_input(password)
        self.__render_team_forename_input(forename)
        self.__render_team_surname_input(surname)
        self.__render_team_date_of_birth_input(date_of_birth)
        self.__render_team_role_input(role)
        self.__render_edit_team_save(username, password, forename, surname, date_of_birth, role)
        self.__render_team_back_input()
        self.__apply_frame()

    def __render_team_username_input(self, username):
        Label(self.__body_frame, text="Username").grid(row=0, column=0)
        Entry(self.__body_frame, textvariable=username).grid(row=0, column=1)

    def __render_team_password_input(self, password):
        Label(self.__body_frame, text="Password").grid(row=1, column=0)
        Entry(self.__body_frame, textvariable=password).grid(row=1, column=1)

    def __render_team_forename_input(self, forename):
        Label(self.__body_frame, text="Forename").grid(row=2, column=0)
        Entry(self.__body_frame, textvariable=forename).grid(row=2, column=1)

    def __render_team_surname_input(self, surname):
        Label(self.__body_frame, text="Surname").grid(row=3, column=0)
        Entry(self.__body_frame, textvariable=surname).grid(row=3, column=1)

    def __render_team_date_of_birth_input(self, date_of_birth):
        date_of_birth.set("22/12/1998")
        Label(self.__body_frame, text="DOB").grid(row=4, column=0)
        Calendar(self.__body_frame, date_pattern="yyyy-mm-dd", textvariable=date_of_birth, selectmode='day').grid(row=4, column=1)

    def __render_team_role_input(self, role):
        roles = RolesManager(self.__database).get_roles()
        role.set(roles[0])

        Label(self.__body_frame, text="Role").grid(row=5, column=0)
        OptionMenu(self.__body_frame, role, *roles).grid(row=5, column=1)

    def __render_add_team_save(self, forename, surname, date_of_birth):
        command_save = partial(
            self.__add_team_process,
            forename,
            surname,
            date_of_birth
        )

        Button(self.__actions_frame, text="Save", command=command_save).grid(row=0, column=0)

    def __add_team_process(self, forename, surname, date_of_birth):
        TeamManager(self.__database).add_team(
            forename.get(),
            surname.get(),
            date_of_birth.get()
        )

        self.__render_team()

    def __render_edit_team_save(self, username, password, forename, surname, date_of_birth, role):
        command_save = partial(
            self.__edit_team_process,
            username,
            password,
            forename,
            surname,
            date_of_birth,
            role
        )

        Button(self.__actions_frame, text="Save", command=command_save).grid(row=0, column=0)

    def __edit_team_process(self, username, password, forename, surname, date_of_birth, role):
        TeamManager(self.__database).edit_team(
            username.get(),
            password.get(),
            forename.get(),
            surname.get(),
            date_of_birth.get(),
            role.get()
        )

        self.__render_team()

    def __render_team_back_input(self):
        command_back = partial(self.__render_team)
        Button(self.__actions_frame, text="Back", command=command_back).grid(row=0, column=1)

    def __render_menu(self):
        instructions = (
            "Welcome to the Menu Page.\n "
            "BLABLABLA."
        )

        self.__clear_window()
        self.__render_instructions(instructions)
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
            self.__body_frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_menu_body(self):
        for i in MenuManager(self.__database).get_menu():
            self.__treeview.insert("", "end", values=(
                i[1],
                f"£{i[2]}",
                f"{i[3]} cals"
            ))

    def __menu_nutrition_procedure(self, event):
        self.__render_nutrition(self.__get_treeview_event())

    def __render_menu_back(self):
        command_logout = partial(self.__render_actions)
        Button(self.__actions_frame, text="Back", command=command_logout).grid(row=0, column=0)

    def __render_nutrition(self, nutrition):
        instructions = (
            f"Welcome to the {nutrition} Nutrition Page.\n "
            "BLABLABLA."
        )

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_nutrition_treeview(nutrition)
        self.__render_nutrition_back()
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
            self.__body_frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            self.__treeview.heading(i, text=i)

    def __render_nutrition_body(self, nutrition):
        for i in NutritionManager(self.__database).get_nutrition(nutrition):
            self.__treeview.insert("", "end", values=(
                i[1],
                f"x{i[2]}",
                f"{i[3]}g",
                f"{i[4]} cals"
            ))

    def __render_nutrition_back(self):
        command_logout = partial(self.__render_menu)
        Button(self.__actions_frame, text="Back", command=command_logout).grid(row=0, column=0)