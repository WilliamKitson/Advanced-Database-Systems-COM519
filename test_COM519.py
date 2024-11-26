#  Copyright (c) 2024. William E. Kitson

from login_manager import LoginManager
import sqlite3

database = "4kitsw10_COM519_database"

def test_login_successful():
    cursor = sqlite3.connect(database).cursor()

    cursor.execute(
        "SELECT * "
        "FROM Staff"
    )

    for row in cursor.fetchall():
        username = row[1]
        password = row[2]
        assert(LoginManager(database).login(username, password) == True)

def test_login_unsuccessful():
    cursor = sqlite3.connect(database).cursor()

    cursor.execute(
        "SELECT * "
        "FROM Staff"
    )

    for row in cursor.fetchall():
        username = f"{row[1]}_blablabla"
        password = f"{row[2]}_blablabla"
        assert(LoginManager(database).login(username, password) == False)