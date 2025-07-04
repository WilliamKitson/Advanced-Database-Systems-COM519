#  Copyright (c) 2024. William E. Kitson

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from tkcalendar import Calendar
from functools import partial
from login_manager import LoginManager
from team_manager import TeamManager
from roles_manager import RolesManager
from menu_manager import MenuManager
from nutrition_manager import NutritionManager
from backup_xml import BackupXML
from image_writer import ImageWriter
from input_validator import InputValidator

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
        login_manager = LoginManager(self.__database)

        if login_manager.login(username.get(), password.get()):
            self.__render_actions()
            return

        if login_manager.get_suspicious():
            messagebox.showwarning(
                "Login Suspicious",
                "The username or password you supplied are suspicious. "
                "I do not appreciate SQL injection attacks!"
            )

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
            BackupXML(self.__database).backup()

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
            "Id",
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
                i[2],
                f"{i[3]} years",
                f"{i[4]} years",
                i[5]
            ))

    def __edit_team_procedure(self, event):
        self.__render_team_edit(self.__get_treeview_event())

    def __render_team_add(self):
        command_add = partial(self.__render_add_team)
        Button(self.__actions_frame, text="Add", command=command_add).grid(row=1, column=0)

    def __render_add_team(self):
        instructions = "Welcome to the Add Team Member Page.\n "

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
        instructions = "Welcome to the Edit Team Member Page.\n "

        staff_at_id = TeamManager(self.__database).get_staff_at(team_id)

        username = StringVar()
        username.set(staff_at_id[1])

        password = StringVar()
        password.set("DefaultPassword")

        forename = StringVar()
        forename.set(staff_at_id[2])

        surname = StringVar()
        surname.set(staff_at_id[3])

        date_of_birth = StringVar()
        date_of_birth.set(staff_at_id[4])

        role = StringVar()
        role.set(staff_at_id[5])

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_team_username_input(username)
        self.__render_team_password_input(password)
        self.__render_team_forename_input(forename)
        self.__render_team_surname_input(surname)
        self.__render_team_date_of_birth_input(date_of_birth)
        self.__render_team_role_input(role)
        self.__render_edit_team_save(username, password, forename, surname, date_of_birth, team_id, role)
        self.__render_edit_team_delete(team_id)
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
        date_of_birth.set("1998-12-22")
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
        team_manager = TeamManager(self.__database)

        team_manager.add_team(
            forename.get(),
            surname.get(),
            date_of_birth.get()
        )

        if team_manager.get_suspicious():
            messagebox.showwarning(
                "Suspicious Add",
                "The you supplied are suspicious. I do not appreciate SQL injection attacks!"
            )

        self.__render_team()

    def __render_edit_team_save(self, username, password, forename, surname, date_of_birth, staff_id, role):
        command_save = partial(
            self.__edit_team_process,
            username,
            password,
            forename,
            surname,
            date_of_birth,
            staff_id,
            role
        )

        Button(self.__actions_frame, text="Save", command=command_save).grid(row=0, column=0)

    def __render_edit_team_delete(self, staff_id):
        command_delete = partial(self.__team_delete_process, staff_id)
        Button(self.__actions_frame, text="Delete", command=command_delete).grid(row=0, column=1)

    def __team_delete_process(self, staff_id):
        TeamManager(self.__database).delete_team(staff_id)
        self.__render_team()

    def __edit_team_process(self, username, password, forename, surname, date_of_birth, staff_id, role):
        if not InputValidator().valid_password(password.get()):
            messagebox.showwarning(
                "Password Invalid",
                "The password you have passed is not valid. Please try again."
            )

            return

        team_manager = TeamManager(self.__database)

        team_manager.edit_team(
            username.get(),
            password.get(),
            forename.get(),
            surname.get(),
            date_of_birth.get(),
            staff_id,
            role.get()
        )

        if team_manager.get_suspicious():
            messagebox.showwarning(
                "Suspicious Edit",
                "The values you supplied are suspicious. I do not appreciate SQL injection attacks!"
            )

        self.__render_team()

    def __render_team_back_input(self):
        command_back = partial(self.__render_team)
        Button(self.__actions_frame, text="Back", command=command_back).grid(row=0, column=2)

    def __render_menu(self):
        instructions = (
            "Welcome to the Menu Page.\n "
            "Here, you can add and edit menu items, you can also save an associated image to the database."
        )

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_menu_treeview()
        self.__render_menu_add_input()
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
            "Category",
            "RSP",
            "Calories",
            "Weight"
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
                i[0],
                f"£{i[2]}",
                f"{i[3]} cals",
                f"{i[4]}g"
            ))

    def __menu_nutrition_procedure(self, event):
        self.__render_menu_edit(self.__get_treeview_event())

    def __render_menu_add_input(self):
        command_logout = partial(self.__render_menu_add)
        Button(self.__actions_frame, text="Add", command=command_logout).grid(row=0, column=0)

    def __render_menu_back(self):
        command_logout = partial(self.__render_actions)
        Button(self.__actions_frame, text="Back", command=command_logout).grid(row=0, column=1)

    def __render_menu_add(self):
        instructions = f"Welcome to the Menu Add page.\n "

        category = StringVar()
        name = StringVar()
        price = StringVar()
        time = StringVar()

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_menu_add_categories(category)
        self.__render_menu_add_name(name)
        self.__render_menu_add_price(price)
        self.__render_menu_add_time(time)
        self.__render_menu_add_save(category, name, price, time)
        self.__render_menu_add_back()
        self.__apply_frame()

    def __render_menu_add_categories(self, category):
        categories = MenuManager(self.__database).get_categories()
        category.set(categories[0])

        Label(self.__body_frame, text="Category").grid(row=0, column=0)
        OptionMenu(self.__body_frame, category, *categories).grid(row=0, column=1)

    def __render_menu_add_name(self, name):
        Label(self.__body_frame, text="Name").grid(row=1, column=0)
        Entry(self.__body_frame, textvariable=name).grid(row=1, column=1)

    def __render_menu_add_price(self, price):
        Label(self.__body_frame, text="Price").grid(row=2, column=0)
        Entry(self.__body_frame, textvariable=price).grid(row=2, column=1)

    def __render_menu_add_time(self, time):
        Label(self.__body_frame, text="Cook Time").grid(row=3, column=0)
        Entry(self.__body_frame, textvariable=time).grid(row=3, column=1)

    def __render_menu_add_save(self, category, name, price, time):
        command_save = partial(self.__menu_add_process, category, name, price, time)
        Button(self.__actions_frame, text="Save", command=command_save).grid(row=0, column=0)

    def __menu_add_process(self, category, name, price, time):
        menu_manager = MenuManager(self.__database)

        menu_manager.add_menu(
            category.get(),
            name.get(),
            price.get(),
            time.get()
        )

        if menu_manager.get_suspicious():
            messagebox.showwarning(
                "Suspicious Add",
                "The values you supplied are suspicious. I do not appreciate SQL injection attacks!"
            )

        self.__render_menu()

    def __render_menu_add_back(self):
        command_logout = partial(self.__render_menu)
        Button(self.__actions_frame, text="Back", command=command_logout).grid(row=0, column=2)

    def __render_menu_edit(self, menu_id):
        instructions = f"Welcome to the Menu Edit page.\n "

        menu_item_at = MenuManager(self.__database).get_menu_at(menu_id)

        category = StringVar()
        category.set(menu_item_at[1])

        name = StringVar()
        name.set(menu_item_at[2])

        price = StringVar()
        price.set(menu_item_at[3])

        time = StringVar()
        time.set(menu_item_at[4])

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_menu_add_categories(category)
        self.__render_menu_add_name(name)
        self.__render_menu_add_price(price)
        self.__render_menu_add_time(time)
        self.__render_menu_edit_image(menu_id)

        img = ImageTk.PhotoImage(ImageWriter("4kitsw10_COM519_database").load(name.get()))
        panel = Label(self.__body_frame, image=img)
        panel.photo = img
        panel.grid(row=5, column=0)

        self.__render_menu_edit_save(menu_id, category, name, price, time)
        self.__render_menu_edit_nutrition(menu_id)
        self.__render_menu_add_back()
        self.__apply_frame()

    def __render_menu_edit_image(self, menu_id):
        command_image = partial(ImageWriter(self.__database).write, menu_id)
        Button(self.__body_frame, text="Edit Image", command=command_image).grid(row=4, column=0)

    def __render_menu_edit_save(self, menu_id, category, name, price, time):
        command_save = partial(self.__menu_edit_procedure, menu_id, category, name, price, time)
        Button(self.__actions_frame, text="Save", command=command_save).grid(row=0, column=0)

    def __menu_edit_procedure(self, menu_id, category, name, price, time):
        menu_manager = MenuManager(self.__database)

        menu_manager.edit_menu(
            menu_id,
            category.get(),
            name.get(),
            price.get(),
            time.get()
        )

        if menu_manager.get_suspicious():
            messagebox.showwarning(
                "Suspicious Edit",
                "The values you supplied are suspicious. I do not appreciate SQL injection attacks!"
            )

        self.__render_menu()

    def __render_menu_edit_nutrition(self, nutrition):
        command_nutrition = partial(self.__render_nutrition, nutrition)
        Button(self.__actions_frame, text="Nutrition", command=command_nutrition).grid(row=0, column=1)

    def __render_nutrition(self, nutrition):
        instructions = f"Welcome to the {nutrition} Nutrition Page.\n "

        self.__clear_window()
        self.__render_instructions(instructions)
        self.__render_nutrition_treeview(nutrition)
        self.__render_menu_add_back()
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