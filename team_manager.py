#  Copyright (c) 2024. William E. Kitson

import sqlite3

class TeamManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()

    def get_team(self):
        self.__cursor.execute(
            "SELECT * "
            "FROM View_Team_Members"
        )

        return self.__cursor.fetchall()

    def get_roles(self):
        self.__cursor.execute(
            "SELECT Title "
            "FROM Roles"
        )

        return self.__cursor.fetchall()

    def add_team(self, forename, surname, date_of_birth, role):
        query = (
            "INSERT INTO Staff (Username, Password, Forename, Surname, DOB)"
            "VALUES (?, ?, ?, ?, ?)"
        )

        parameters = (
            f"{forename}_{surname}",
            f"{forename}{surname}{date_of_birth}",
            forename,
            surname,
            date_of_birth
        )

        self.__cursor.execute(
            query,
            parameters
        )

        self.__database.commit()

    def __del__(self):
        self.__database.close()