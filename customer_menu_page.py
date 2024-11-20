from tkinter import *
from treeview_page import TreeviewPage
from dish_neutrition_page import DishNutritionPage

class CustomerMenuPage(TreeviewPage):
    def __init__(self, database):
        columns = "Name", "RSP", "Calories"
        TreeviewPage.__init__(self, database, "customer menu", columns)

    def render(self):
        self.__render_treeview()
        self.__render_add()
        self._window.mainloop()

    def __render_treeview(self):
        self._cursor.execute(
            "SELECT * "
            "FROM Customer_Facing_Menu"
        )

        for row in self._cursor.fetchall():
            self._treeview.insert("", "end", values=(
                row[1],
                f"£{row[2]}",
                f"{row[3]} cals"
            ))

        self._treeview.bind("<Double-1>", self.__item_submenu)
        self._treeview.grid(row=0, column=0)

    def __render_add(self):
        Button(self._window, text="Add Dish").grid(row=1, column=0)

    def __item_submenu(self, event):
        DishNutritionPage(
            self._database,
            self.__get_clicked_item()
        ).render()

    def __get_clicked_item(self):
        item = self._treeview.selection()[0]
        return self._treeview.item(item, "values")[0]