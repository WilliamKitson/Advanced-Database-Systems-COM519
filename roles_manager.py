#  Copyright (c) 2024. William E. Kitson

import sqlite3

class RolesManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()

    def get_roles(self):
        self.__cursor.execute(
            "SELECT Title "
            "FROM Roles"
        )

        roles = []

        for i in self.__cursor.fetchall():
            roles.append(i[0])

        return roles

    def __del__(self):
        self.__database.close()