from page import Page

class DishNutritionPage(Page):
    def __init__(self, database, dish):
        columns = "Ingredient", "Quantity", "Total Weight", "Total Calories"
        Page.__init__(self, database, f"{dish} nutrition", columns)
        self.__dish = dish

    def render(self):
        self._cursor.execute(
            "SELECT * "
            "FROM Menu_Item_Neutrition "
            "WHERE Menu_Item_Neutrition.Menu_Item="
            f"'{self.__dish}'"
        )

        for row in self._cursor.fetchall():
            self._treeview.insert("", "end", values=(
                row[1],
                row[2],
                f"{row[3]}g",
                f"{row[4]} cals"
            ))

        self._treeview.pack(fill="x")
        self._window.mainloop()