import sqlite3

class NutritionManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()

    def get_nutrition(self, nutrition):
        query = ("SELECT * "
            "FROM Menu_Item_Neutrition "
            "WHERE Menu_Item_Neutrition.Menu_Item=?"
        )

        self.__cursor.execute(query, (nutrition,))

        return self.__cursor.fetchall()

    def __del__(self):
        self.__database.close()