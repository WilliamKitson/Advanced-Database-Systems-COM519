import sqlite3
from tkinter import ttk

class CustomerMenuPage:
    def __init__(self, window):
        self.__window = window
        self.__treeview = self.__initialise_treeview()
        self.__cursor = self.__initialise_cursor()

    def __initialise_treeview(self):
        headers = (
            'Name',
            'RSP',
            'Calories',
            "Order"
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
            "FROM Customer_Facing_Menu"
        )

        for row in self.__cursor.fetchall():
            self.__treeview.insert("", "end", values=(
                row[1],
                f"£{row[2]}",
                f"{row[3]} cals",
                "temp"
            ))

        self.__treeview.bind("<Double-1>", self.__item_submenu)
        self.__treeview.pack(fill="x")

    def __item_submenu(self, event):
        self.__cursor.execute(
            "SELECT * "
            "FROM Menu_Item_Neutrition "
            "WHERE Menu_Item_Neutrition.Menu_Item="
            f"'{self.__get_clicked_item()}'"
        )

        for row in self.__cursor.fetchall():
            print(row)

    def __get_clicked_item(self):
        item = self.__treeview.selection()[0]
        return self.__treeview.item(item, "values")[0]