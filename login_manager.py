#  Copyright (c) 2024. William E. Kitson

import sqlite3
import hashlib
from injection_detector import InjectionDetector

class LoginManager:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()
        self.__suspicious = False

    def login(self, username, password):
        self.__calculate_suspicious(username, password)

        if self.__suspicious:
            return False

        query = (
            "SELECT Staff.Staff_Id "
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

    def __calculate_suspicious(self, username, password):
        if InjectionDetector().suspicious(username):
            self.__suspicious = True
            return

        if InjectionDetector().suspicious(password):
            self.__suspicious = True
            return

        self.__suspicious = False

    def __get_hashed_password(self, password):
        password_hash = hashlib.sha256(password.encode())
        return password_hash.hexdigest()

    def get_suspicious(self):
        return self.__suspicious

    def __del__(self):
        self.__database.close()