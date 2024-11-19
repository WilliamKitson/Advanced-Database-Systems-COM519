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
        username = row[0]
        password = row[1]
        assert(LoginManager().breach(username, password) == True)