import sqlite3

class LoginManager:
    def __init__(self, database):
        self.__database = database
        self.__cursor = sqlite3.connect(database).cursor()

    def breach(self, username, password):
        query = (
            "SELECT * "
            "FROM Staff "
            "WHERE Username = ? "
            "AND Password = ? "
        )

        self.__cursor.execute(query, (username.get(), password.get()))

        for row in self.__cursor.fetchall():
            return True

        return False