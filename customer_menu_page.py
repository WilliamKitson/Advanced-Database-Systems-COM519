from page import Page
from dish_neutrition_page import DishNutritionPage

class CustomerMenuPage(Page):
    def __init__(self, database):
        columns = "Name", "RSP", "Calories"
        Page.__init__(self, database, "customer menu page", columns)

    def render(self):
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
        self._treeview.pack(fill="x")
        self._window.mainloop()

    def __item_submenu(self, event):
        DishNutritionPage(
            self._database,
            self._window,
            self.__get_clicked_item()
        ).render()

    def __get_clicked_item(self):
        item = self._treeview.selection()[0]
        return self._treeview.item(item, "values")[0]