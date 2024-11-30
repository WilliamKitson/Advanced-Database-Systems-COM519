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

        password_hash = hashlib.sha256(password.encode())

        parameters = (
            username,
            password_hash.hexdigest()
        )

        self.__cursor.execute(query, parameters)

        for row in self.__cursor.fetchall():
            return True

        return False

    def __del__(self):
        self.__database.close()