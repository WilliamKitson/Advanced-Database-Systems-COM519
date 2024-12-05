#  Copyright (c) 2024. William E. Kitson

import sqlite3
import hashlib
from injection_detector import InjectionDetector

class TeamManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()
        self.__suspended = False

    def get_team(self):
        self.__cursor.execute(
            "SELECT * "
            "FROM View_Team_Members"
        )

        return self.__cursor.fetchall()

    def add_team(self, forename, surname, date_of_birth):
        inputs = [
            forename,
            surname,
            date_of_birth
        ]

        self.__calculate_suspicious(inputs)

        if self.__suspicious:
            return

        query = (
            "INSERT INTO Staff (Username, Password, Forename, Surname, DOB)"
            "VALUES (?, ?, ?, ?, ?)"
        )

        parameters = (
            f"{forename}_{surname}",
            self.__get_hashed_password(f"{forename}{surname}{date_of_birth}"),
            forename,
            surname,
            date_of_birth
        )

        self.__cursor.execute(query, parameters)
        self.__database.commit()

    def __calculate_suspicious(self, inputs):
        for i in inputs:
            if InjectionDetector().suspicious(i):
                self.__suspicious = True
                return

        self.__suspicious = False

    def __get_hashed_password(self, password):
        password_hash = hashlib.sha256(password.encode())
        return password_hash.hexdigest()

    def edit_team(self, username, password, forename, surname, date_of_birth, staff_id, role):
        inputs = [
            username,
            password,
            forename,
            surname,
            date_of_birth,
            staff_id,
            role
        ]

        self.__calculate_suspicious(inputs)

        if self.__suspicious:
            return

        self.__edit_team_staff(username, password, forename, surname, date_of_birth, staff_id)
        self.__edit_team_role(role, staff_id)

    def __edit_team_staff(self, username, password, forename, surname, date_of_birth, staff_id):
        query = (
            "UPDATE "
            "Staff "
            "SET "
            "Username = ?, "
            "Password = ?, "
            "Forename = ?, "
            "Surname = ?, "
            "DOB = ? "
            "WHERE Staff_Id = ?"
        )

        parameters = (
            username,
            self.__get_hashed_password(password),
            forename,
            surname,
            date_of_birth,
            staff_id,
        )

        self.__cursor.execute(query, parameters)
        self.__database.commit()

    def __edit_team_role(self, role, staff_id):
        query = (
            "UPDATE Staff_Roles SET "
            "Role_Id = ( "         
            "SELECT Role_Id "
            "FROM Roles "
            "WHERE Roles.Title = ? "
            ") "
            "WHERE Staff_Id = ?"
        )

        parameters = (
            role,
            staff_id,
        )

        self.__cursor.execute(query, parameters)
        self.__database.commit()

    def delete_team(self, staff_id):
        query = (
            "DELETE FROM Staff "
            "WHERE Staff_Id = ?"
        )

        self.__cursor.execute(query, (staff_id,))
        self.__database.commit()

    def get_staff_at(self, staff_id):
        query = (
            "SELECT * "
            "FROM Staff_Edit_Data "
            "WHERE Staff_Id = ?"
        )

        self.__cursor.execute(
            query,
            (staff_id,)
        )

        for i in self.__cursor.fetchall():
            return i

    def get_suspicious(self):
        return self.__suspicious

    def __del__(self):
        self.__database.close()