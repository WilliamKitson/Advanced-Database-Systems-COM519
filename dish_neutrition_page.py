import sqlite3

class DishNutritionPage:
    def __init__(self, window, dish):
        self.__window = window
        self.__cursor = self.__initialise_cursor()
        self.__dish = dish

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
            print(row)