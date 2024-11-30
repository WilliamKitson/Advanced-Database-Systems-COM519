#  Copyright (c) 2024. William E. Kitson

import sqlite3
import hashlib

class LoginManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()

    def login(self, username, password):
        query = (
            "SELECT * "
            "FROM Staff "
            "WHERE Username = ? "
            "AND Password = ? "
        )

        parameters = (
            username,
            self.__get_hashed_password(password),
        )

        self.__cursor.execute(query, parameters)

        for row in self.__cursor.fetchall():
            return True

        return False

    def __get_hashed_password(self, password):
        password_hash = hashlib.sha256(password.encode())
        return password_hash.hexdigest()

    def __del__(self):
        self.__database.close()