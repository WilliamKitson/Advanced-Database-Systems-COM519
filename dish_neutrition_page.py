import sqlite3
from tkinter import ttk

class DishNutritionPage:
    def __init__(self, window, dish):
        self.__window = window
        self.__treeview = self.__initialise_treeview()
        self.__cursor = self.__initialise_cursor()
        self.__dish = dish

    def __initialise_treeview(self):
        headers = (
            'Ingredient',
            'Quantity',
            'Total Weight',
            'Total Calories'
        )

        tree = ttk.Treeview(self.__window, columns=headers, show='headings')

        for i in headers:
            tree.heading(i, text=i)

        return tree

    @staticmethod
    def __initialise_cursor():
        connection_obj = sqlite3.connect("4kitsw10_COM519_database")
        return connection_obj.cursor()

    def render(self):
        self.__cursor.execute(
            "SELECT * "
            "FROM Menu_Item_Neutrition "
            "WHERE Menu_Item_Neutrition.Menu_Item="
            f"'{self.__dish}'"
        )

        for row in self.__cursor.fetchall():
            self.__treeview.insert("", "end", values=(
                row[1],
                row[2],
                f"{row[3]}g",
                f"{row[4]} cals"
            ))

            self.__treeview.pack(fill="x")