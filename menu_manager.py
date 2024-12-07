#  Copyright (c) 2024. William E. Kitson

import sqlite3
from injection_detector import InjectionDetector

class MenuManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()
        self.__suspended = False

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
        inputs = [
            category,
            name,
            price,
            time
        ]

        self.__calculate_suspicious(inputs)

        if self.__suspicious:
            return

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

    def __calculate_suspicious(self, inputs):
        for i in inputs:
            if InjectionDetector().suspicious(i):
                self.__suspicious = True
                return

        self.__suspicious = False

    def edit_menu(self, menu_id, category, name, price, time):
        inputs = [
            category,
            name,
            price,
            time
        ]

        self.__calculate_suspicious(inputs)

        if self.__suspicious:
            return

        query = (
            "UPDATE "
            "Menu "
            "SET "
            "Category_Id = ( "
            "SELECT Category_Id "
            "FROM Categories "
            "WHERE Name = ? "
            "), "
            "Name = ?, "
            "RSP = ?, "
            "Cook_Time = ? "
            "WHERE Name = ? "
        )

        parameters = (category, name, price, time, menu_id)

        self.__cursor.execute(query, parameters)
        self.__database.commit()

    def get_suspicious(self):
        return self.__suspicious

    def __del__(self):
        self.__database.close()