from tkinter import *
from treeview_page import TreeviewPage

class DishNutritionPage(TreeviewPage):
    def __init__(self, database, dish):
        columns = "Ingredient", "Quantity", "Total Weight", "Total Calories"
        TreeviewPage.__init__(self, database, f"{dish} nutrition", columns)
        self.__dish = dish

    def render(self):
        self.__render_treeview()
        self.__render_add()
        self._window.mainloop()

    def __render_treeview(self):
        self._cursor.execute(
            "SELECT * "
            "FROM Menu_Item_Neutrition "
            "WHERE Menu_Item_Neutrition.Menu_Item=?",
            (self.__dish,)
        )

        for row in self._cursor.fetchall():
            self._treeview.insert("", "end", values=(
                row[1],
                row[2],
                f"{row[3]}g",
                f"{row[4]} cals"
            ))

        self._treeview.grid(row=0, column=0)

    def __render_add(self):
        Button(self._window, text="Add Ingredient").grid(row=1, column=0)