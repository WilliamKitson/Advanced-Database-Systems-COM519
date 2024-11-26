import sqlite3

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

        self.__cursor.execute(query, (username, password))

        for row in self.__cursor.fetchall():
            return True

        return False

    def __del__(self):
        self.__database.close()