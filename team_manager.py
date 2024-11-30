#  Copyright (c) 2024. William E. Kitson

import sqlite3
import hashlib

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

    def add_team(self, forename, surname, date_of_birth):
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

    def __get_hashed_password(self, password):
        password_hash = hashlib.sha256(password.encode())
        return password_hash.hexdigest()

    def edit_team(self, username, password, forename, surname, date_of_birth, staff_id, role):
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
            "FROM Staff "
            "LEFT JOIN Staff_Roles ON Staff.Staff_Id = Staff_Roles.Staff_Id "
            "LEFT JOIN Roles ON Staff_Roles.Role_Id = Roles.Role_Id "
            "WHERE Staff.Staff_Id = ?"
        )

        self.__cursor.execute(
            query,
            (staff_id,)
        )

        for i in self.__cursor.fetchall():
            return (
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[10]
            )

    def __del__(self):
        self.__database.close()