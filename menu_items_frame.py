import sqlite3
from tkinter import *
from tkinter import ttk
from dish_nutrition_frame import DishNutritionFrame

class MenuItemsFrame:
    def __init__(self, database, window):
        self.__frame = Frame(window)
        self.__database = database
        self.__window = window
        self.__cursor = sqlite3.connect(database).cursor()
        self.__treeview = None

    def render(self):
        self.__treeview = self.__render_headings()
        self.__treeview.grid(row=0, column=0)
        self.__frame.grid(row=0, column=0)

    def __render_headings(self):
        columns = [
            "Name",
            "RSP",
            "Calories"
        ]

        treeview = ttk.Treeview(
            self.__frame,
            columns=columns,
            show="headings"
        )

        for i in columns:
            treeview.heading(i, text=i)

        return self.__render_body(treeview)

    def __render_body(self, treeview):
        self.__cursor.execute(
            "SELECT * "
            "FROM Customer_Facing_Menu"
        )

        for row in self.__cursor.fetchall():
            treeview.insert("", "end", values=(
                row[1],
                f"£{row[2]}",
                f"{row[3]} cals"
            ))

        treeview.bind("<Double-1>", self.__item_submenu)
        return treeview

    def __item_submenu(self, event):
        DishNutritionFrame(
            self.__database,
            self.__window,
            self.__get_clicked_item()
        ).render()

    def __get_clicked_item(self):
        item = self.__treeview.selection()[0]
        return self.__treeview.item(item, "values")[0]

    def get_frame(self):
        return self.__frame

    def get_resolution(self):
        return f"{self.__frame.winfo_width()}x{self.__frame.winfo_height()}"