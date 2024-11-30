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

    def get_menu_at(self, menu_id):
        query = (
            "SELECT * "
            "FROM Menu "
            "WHERE Name = ? "
        )

        self.__cursor.execute(query, (menu_id,))

        for i in self.__cursor.fetchall():
            return i

    def get_categories(self):
        self.__cursor.execute(
            "SELECT Name "
            "FROM Categories"
        )

        categories = []

        for i in self.__cursor.fetchall():
            categories.append(i[0])

        return categories

    def add_menu(self, category, name, price, time):
        query = (
            "INSERT INTO Menu (Category_Id, Name, RSP, Cook_Time)"
            "VALUES (("     
            "SELECT Category_Id "
            "FROM Categories "
            "WHERE Name = ? "
            "), ?, ?, ?)"
        )

        parameters = (
            category,
            name,
            price,
            time
        )

        self.__cursor.execute(query, parameters)
        self.__database.commit()

    def edit_menu(self, menu_id, category, name, price, time):
        print(menu_id, category, name, price, time)

    def __del__(self):
        self.__database.close()