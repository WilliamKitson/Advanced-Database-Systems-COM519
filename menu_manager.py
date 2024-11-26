#  Copyright (c) 2024. William E. Kitson

import sqlite3

class MenuManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()

    def get_menu(self):
        self.__cursor.execute(
            "SELECT * "
            "FROM Customer_Facing_Menu"
        )

        return self.__cursor.fetchall()

    def __del__(self):
        self.__database.close()